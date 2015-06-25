__author__ = 'shawn'
from midi.lib import playMidiFile
from midi.lib import midi_stream
from midi.lib import midi_from_message


def play_file(file_name):
    return playMidiFile.play_music(file_name)


def start_keyboard_stream(file_name="", display=True):
    midi_stream.start_midi_stream(file_name, display)


def create_file_from_list(messages, file_name='new_song.mid'):
    midi_from_message.from_message(messages, file_name)


def save_and_play(file_name="new_song.mid", display=True):
    start_keyboard_stream(file_name, display)
    play_file(file_name)
