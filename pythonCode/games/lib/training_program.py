__author__ = 'shawn'

import pygame, sys
import time
from random import randint
import mido
from threading import Thread
from midi import logic
from mido.midifiles import *


class PlayToContinue:
    def __init__(self):
        self.__states = {"menu": 0, "play": 1, "playBack": 2}
        self.__state = self.__states["menu"]
        self.__bpm = 0
        self.__notes = []
        self.__loading = 0
        self.__note_start_time = 0
        self.__current_note_to_play = 0
        self.__recording = False
        self.__playing_game = False
        self.__of_name = ""

        self.__done = False
        self.__key_mod_size = logic.get_length_notes()

        pygame.init()
        pygame.mixer.init(44100, -16, 2, 1024)
        self.__screen = pygame.display.set_mode((640, 480))
        self.__clock = pygame.time.Clock()

        self.__note_font = pygame.font.Font(None, 148)
        self.__info_font = pygame.font.Font(None, 28)

        self.__display_center_message = self.__note_font.render("", True, (0, 0, 0))
        self.commands = [
            self.__info_font.render("Press esc to quit", True,(205, 92, 92)),
            self.__info_font.render("Press s to start", True,(205, 92, 92)),
            self.__info_font.render("Press p to play back sound ", True,(205, 92, 92))]

    def start(self, bpm, note_file_name, out_file_name):
        self.__of_name = out_file_name
        self.__read_note_file(note_file_name)
        self.__bpm = bpm
        if not self.__screen: raise NotImplementedError("Class Not Initilized.")
        self.__display_bpm = self.__info_font.render("bpm: " + str(self.__bpm), True,(205, 92, 92))
        while not self.__done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__done = True
                    self.__set_and_update_center_message("hit any note")
                    continue
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.__state == self.__states["menu"]:
                        self.__done = True
                        self.__set_and_update_center_message("hit any note")
                        continue
                    elif self.__state == self.__states["play"]:
                        self.__display_center_message = self.__note_font.render("", True, (0, 0, 0))
                        self.__state = self.__states["menu"]
                if self.__state == self.__states["menu"]:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        self.__state = self.__states["play"]
                        self.__playing_game = True
                        self.__loading = time.time()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.__state = self.__states["playBack"]
                        self.__loading = time.time()
                        self.__playing_game = True

            if self.__state == self.__states["play"]:
                self.__play_screen()
            if self.__state == self.__states["menu"]:
                self.__menu_screen()
            if self.__state == self.__states["playBack"]:
                self.__playback_screen()
            pygame.display.flip()
            self.__clock.tick(60)

    def __playback_screen(self):
        if not self.__playing_game:
            self.__state = self.__states["menu"]
            return
        self.__screen.fill((255, 255, 255))
        if time.time() - self.__loading < 3:
            self.__set_and_update_center_message("Starting In: " + str(round(3 - (time.time() - self.__loading))))
            self.__note_start_time = time.time()
        else:
            if not self.__recording:
                self.__play_music_from_file('new_song.mid')
                self.__recording = True
            self.__new_note()

    def __display_menu_commands(self):
        spacing = 2
        for key, command in enumerate(self.commands):
            self.__screen.blit(command, (2, spacing))
            spacing += command.get_height() + 2

    def __set_and_update_center_message(self, message):
        self.__display_center_message = self.__note_font.render(message, True, (0, 0, 0))
        self.__screen.blit(self.__display_center_message,
                         (320 - self.__display_center_message.get_width() // 2, 240 - self.__display_center_message.get_height() // 2))

    def __menu_screen(self):
        self.__screen.fill((255, 255, 255))
        self.__screen.blit(self.__display_bpm, (self.__screen.get_width() - self.__display_bpm.get_width() - 2, 2))
        self.__set_and_update_center_message("Main Menu")
        self.__display_menu_commands()
        self.__screen.blit(self.__display_center_message,
                         (320 - self.__display_center_message.get_width() // 2, 240 - self.__display_center_message.get_height() // 2))

    def __play_screen(self):
        self.__screen.fill((255, 255, 255))
        if time.time() - self.__loading < 3:
            self.__set_and_update_center_message("Starting In: " + str(round(3 - (time.time() - self.__loading))))
            self.__note_start_time = time.time()
        else:
            if not self.__recording and self.__playing_game:
                Thread(target=self.__start_midi_thread).start()
                print("recording Started")
                self.__recording = True
            if not self.__playing_game:
                self.__play_end()
            else:
                self.__new_note()

    def __play_end(self):
        self.__set_and_update_center_message("hit any note")
        if not self.__recording:
            self.__state = self.__states["menu"]

    def __new_note(self):
        self.__set_and_update_center_message(self.__notes[0][self.__current_note_to_play])
        end_time = self.__bpm/60 * int(self.__notes[1][self.__current_note_to_play])

        self.__display_bpm = self.__info_font.render("New Note In: " + str(round(end_time - (time.time() - self.__note_start_time))), True,(205, 92, 92))
        self.__screen.blit(self.__display_bpm, (self.__screen.get_width() - self.__display_bpm.get_width() - 2, 2))

        if time.time() - self.__note_start_time > end_time:
            self.__current_note_to_play += 1
            self.__note_start_time = time.time()
            if self.__current_note_to_play == len(self.__notes[0]):
                self.__current_note_to_play = 0
                self.__playing_game = False
                self.__display_bpm = self.__info_font.render("bpm: " + str(self.__bpm), True,(205, 92, 92))

    def __start_midi_thread(self):
        last_note = int(round(time.time() * 1000))
        with MidiFile() as mid:
            track = MidiTrack()
            print("Waiting For Keyboard Input ... ")
            with mido.open_input() as inport:
                for msg in inport:
                    if self.__done or not self.__playing_game:
                        self.__recording = False
                        mid.tracks.append(track)
                        mid.save(self.__of_name)
                        print("File Saved!")
                        print("File Location: " + self.__of_name)
                        self.__recording = False
                        return
                    now = int(round(time.time() * 1000))
                    msg.time = now - last_note
                    last_note = now
                    if hasattr(msg, 'velocity') and msg.velocity == 0:
                        msg = Message('note_off', note=msg.note, velocity=msg.velocity, time=msg.time)
                    track.append(msg)

    def __read_note_file(self, file_name):

        beats = []
        notes = []
        with open(file_name) as fp:
            for line in fp:
                line = line.rstrip()
                beat,note = line.split(" ")
                beats.append(beat)
                notes.append(note)
        self.__notes = [notes,beats]

    def __play_music_from_file(self, music_file):
        pygame.mixer.music.set_volume(0.8)
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print ("\nMusic file %s loaded!" % music_file)
        except pygame.error:
            print ("File %s not found! (%s)" % (music_file, pygame.get_error()) )
            return
        pygame.mixer.music.play()
