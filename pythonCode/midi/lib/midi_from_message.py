__author__ = 'shawn'
__author__ = 'shawn'
from mido.midifiles import *

def from_message(messages, file_name):
    with MidiFile() as mid:
        track = MidiTrack()

        for msg in messages:
            track.append(msg)

        mid.tracks.append(track)
        mid.save(file_name)
