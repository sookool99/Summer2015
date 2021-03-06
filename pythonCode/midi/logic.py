__author__ = 'shawn'
from midi.lib import playMidiFile
from midi.lib import midi_stream
from midi.lib import midi_from_message
from midi.lib import keyNotes


def play_file(file_name):
    return playMidiFile.play_music(file_name)


def start_keyboard_stream(file_name="", display=True):
    midi_stream.start_midi_stream(file_name, display)


def create_file_from_list(messages, file_name='new_song.mid'):
    midi_from_message.from_message(messages, file_name)


def save_and_play(file_name="new_song.mid", display=True):
    start_keyboard_stream(file_name, display)
    play_file(file_name)

def get_all_notes():
    return keyNotes.get_all_key_notes()

def get_notes():
    return keyNotes.get_notes()

def get_range_of_notes(start, end):
    return keyNotes.get_all_in_range(start, end)

def get_length_notes():
    return keyNotes.get_length_note()

def get_note_mapping(start, end):
    return keyNotes.get_note_mapping(start, end)

def get_all_note_mapping():
    return keyNotes.get_all_note_mapping()