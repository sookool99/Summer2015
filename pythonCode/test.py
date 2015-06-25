__author__ = 'shawn'
from midi import logic
from mido.midifiles import Message
tmp = [Message('note_on', note=60, velocity=50, time=0), Message('note_off', note=60, velocity=124, time=5000)]

logic.create_file_from_list(tmp,"test123.mid")

logic.play_file("test123.mid")