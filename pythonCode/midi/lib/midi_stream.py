__author__ = 'shawn'

import mido
from mido.midifiles import *
import time
def start_midi_stream(file_name, display):
    last_note = int(round(time.time() * 1000))
    mido.get_output_names()
    port_name = mido.get_input_names()[0]
    print('Starting on port: ' + port_name)
    with MidiFile() as mid:
        track = MidiTrack()
        try:
            print("Waiting For Keyboard Input ... ")
            with mido.open_input(port_name) as inport:
                for msg in inport:
                    now = int(round(time.time() * 1000))
                    msg.time = now - last_note
                    last_note = now
                    if hasattr(msg, 'velocity') and msg.velocity == 0:
                        msg = Message('note_off', note=msg.note, velocity=msg.velocity, time=msg.time)
                    track.append(msg)
                    if display:
                        print(msg)
        except KeyboardInterrupt:
            if file_name:
                print("\nStopping and saving file ... ")
            else:
                print("\nStopping ...")
        finally:
            if file_name:
                print(file_name)
                mid.tracks.append(track)
                mid.save(file_name)
                print("File Saved!")
                print("File Location: " + file_name)
            else:
                print("Done!")
