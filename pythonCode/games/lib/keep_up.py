__author__ = 'shawn'
import pygame, sys
import time
from random import randint
import mido
from threading import Thread
from midi import logic


class PlayToContinue:
    def __init__(self):
        self.last_note_played = 0
        self.all_notes = logic.get_notes()
        self.current_note_to_play = randint(48, 72)
        self.done = False
        self.key_mod_size = logic.get_length_notes()

        self.total_notes_played = 0
        self.total_notes = 0
        self.notes_correct = 0
        self.time_since_note = 0
        self.min_time = 0
        self.note_time_length = 0
        self.incrementer = 0
        self.notes_missed = 0

        self.note_font = None
        self.info_font = None
        self.clock = None
        self.screen = None
        self.display_note = None
        self.display_total_notes = None
        self.display_notes_correct = None
        self.display_notes_missed = None
        self.display_total_notes_played = None

    def start(self, note_length, min_time, inc):
        self.note_time_length = note_length
        self.incrementer = inc
        self.min_time = min_time
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.note_font = pygame.font.Font(None, 148)
        self.info_font = pygame.font.Font(None, 28)

        self.display_total_notes = self.info_font.render("Total Notes: " + str(self.total_notes), True,
                                                         (205, 92, 92))
        self.display_total_notes_played = self.info_font.render("Total Notes Played: " + str(self.total_notes_played),
                                                                True, (205, 92, 92))
        self.display_notes_correct = self.info_font.render("Correct Notes: " + str(self.notes_correct), True,
                                                           (205, 92, 92))

        self.display_notes_missed = self.info_font.render("Missed Notes: " + str(self.notes_missed), True,
                                                          (205, 92, 92))

        print("starting note: " + str(self.current_note_to_play))
        Thread(target=self.start_key_thread).start()

        loading = time.time()
        self.display_note = self.note_font.render("Starting In: " + str(round(3 - (time.time() - loading))), True, (0, 0, 0))

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.done = True
            if  time.time() - loading < 3:
                self.display_note = self.note_font.render("Starting In: " + str(round(3 - (time.time() - loading))), True, (0, 0, 0))
            else:
                if not self.time_since_note:
                    self.display_note = self.note_font.render("Note: " + self.all_notes[self.current_note_to_play], True, (0, 0, 0))
                    self.time_since_note = time.time()
                if time.time() - self.time_since_note > self.note_time_length:
                    self.update_display_note()
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.display_note,
                             (320 - self.display_note.get_width() // 2, 240 - self.display_note.get_height() // 2))

            self.screen.blit(self.display_total_notes, (2, 2))
            self.screen.blit(self.display_total_notes_played, (2, 4 + self.display_total_notes.get_height()))
            self.screen.blit(self.display_notes_correct, (
            2, 6 + self.display_total_notes_played.get_height() + self.display_total_notes.get_height()))
            self.screen.blit(self.display_notes_missed, (2,
                                                         8 + self.display_total_notes_played.get_height() + self.display_notes_correct.get_height() + self.display_total_notes.get_height()))
            pygame.display.flip()
            self.clock.tick(60)

    def update_display_note(self, missed=True):
        self.total_notes += 1
        self.display_total_notes = self.info_font.render("Total Notes: " + str(self.total_notes), True,
                                                         (205, 92, 92))
        self.time_since_note = time.time()
        self.current_note_to_play = randint(48, 72)
        self.display_note = self.note_font.render("Note: " + self.all_notes[self.current_note_to_play], True, (0, 0, 0))
        self.time_since_note = time.time()
        if missed:
            self.notes_missed += 1
        else:
            self.notes_correct += 1
        self.display_notes_missed = self.info_font.render("Missed Notes: " + str(self.notes_missed), True,
                                                          (205, 92, 92))
        if self.note_time_length > self.min_time:
            self.note_time_length -= self.incrementer

    def start_key_thread(self):
        port_name = mido.get_input_names()[0]
        with mido.open_input(port_name) as inport:
            for msg in inport:

                if self.done: return

                if hasattr(msg, 'note') and hasattr(msg, 'velocity') and msg.velocity > 0:
                    print(msg.note)
                    self.total_notes_played += 1
                    self.display_total_notes_played = self.info_font.render(
                        "Total Notes Played: " + str(self.total_notes_played), True,
                        (205, 92, 92))
                if hasattr(msg, 'note') and msg.note % 12 == self.current_note_to_play % 12 and hasattr(msg,
                                                                                                        'velocity') and msg.velocity > 0:
                    self.update_display_note(False)
                    self.notes_correct += 1
                    self.display_notes_correct = self.info_font.render("Correct Notes: " + str(self.notes_correct), True,
                                                           (205, 92, 92))

# game = PlayToContinue()
#
# game.start()
