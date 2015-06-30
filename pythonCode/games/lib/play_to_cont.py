__author__ = 'shawn'
import pygame, sys
import time
from random import randint
import mido
from threading import Thread
from midi import logic


class PlayToContinue:
    def __init__(self):
        self.last_note_played = time.time()
        self.all_notes = logic.get_notes()
        self.current_note_to_play = randint(48, 72)
        self.done = False
        self.key_mod_size = logic.get_length_notes()

        self.total_notes = 0
        self.notes_correct = 0
        self.average_note_time = 0
        self.note_start_time = 0

        self.note_font = None
        self.info_font = None
        self.clock = None
        self.screen = None
        self.display_note = None
        self.display_total_notes = None
        self.display_notes_correct = None
        self.display_average_tries = None
        self.display_average_time = None

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.note_font = pygame.font.Font(None, 156)
        self.info_font = pygame.font.Font(None, 28)

        self.display_note = self.note_font.render("Note: " + self.all_notes[self.current_note_to_play], True, (0, 0, 0))
        self.display_total_notes = self.info_font.render("Total Notes: " + str(self.total_notes), True,
                                                         (205, 92, 92))
        self.display_notes_correct = self.info_font.render("Correct Notes: " + str(self.notes_correct), True,
                                                           (205, 92, 92))
        self.display_average_tries = self.info_font.render("Average Tries: 0", True,
                                                           (205, 92, 92))
        self.display_average_time = self.info_font.render("Average Time: 0", True,
                                                          (205, 92, 92))
        print("starting note: " + str(self.current_note_to_play))
        Thread(target=self.start_key_thread).start()
        self.note_start_time = time.time()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.done = True

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.display_note,
                             (320 - self.display_note.get_width() // 2, 240 - self.display_note.get_height() // 2))
            self.screen.blit(self.display_total_notes, (2, 2))
            self.screen.blit(self.display_notes_correct, (2, 2 + self.display_total_notes.get_height() + 2))
            self.screen.blit(self.display_average_tries, (
                2, 2 + self.display_total_notes.get_height() + 2 + self.display_notes_correct.get_height() + 2))
            self.screen.blit(self.display_average_time, (
                2,
                8 + self.display_total_notes.get_height() + self.display_average_tries.get_height() + self.display_notes_correct.get_height()))
            pygame.display.flip()
            self.clock.tick(60)

    def new_note(self):
        time.sleep(1)
        self.current_note_to_play = randint(48, 72)
        print("new note is: " + str(self.current_note_to_play))
        self.display_note = self.note_font.render("Note: " + self.all_notes[self.current_note_to_play],
                                                  True, (0, 0, 0))
        self.note_start_time = time.time()

    def start_key_thread(self):
        port_name = mido.get_input_names()[0]
        with mido.open_input(port_name) as inport:
            for msg in inport:

                if self.done: return
                if not self.current_note_to_play:
                    print("cannot play notes during this state!")
                    continue

                if hasattr(msg, 'note') and hasattr(msg, 'velocity') and msg.velocity > 0:
                    print(msg.note)
                    self.total_notes += 1
                    self.display_total_notes = self.info_font.render("Total Notes: " + str(self.total_notes), True,
                                                                     (205, 92, 92))
                if hasattr(msg, 'note') and msg.note % 12 == self.current_note_to_play % 12 and hasattr(msg,
                                                                                                        'velocity') and msg.velocity > 0:
                    self.notes_correct += 1
                    self.display_note = self.note_font.render("Correct!!!", True, (0, 128, 0))
                    self.display_notes_correct = self.info_font.render("Correct Notes: " + str(self.notes_correct),
                                                                       True, (205, 92, 92))
                    self.display_average_tries = self.info_font.render(
                        "Average Tries: " + str(round(self.total_notes / self.notes_correct)), True, (205, 92, 92))

                    self.average_note_time += time.time() - self.note_start_time
                    self.display_average_time = self.info_font.render(
                        "Average Time: " + str(round(self.average_note_time / self.notes_correct, 1)) + " seconds",
                        True,
                        (205, 92, 92))
                    self.current_note_to_play = 0
                    Thread(target=self.new_note()).start()


# game = PlayToContinue()
#
# game.start()
