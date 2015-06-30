__author__ = 'shawn'
import mido
from mido.midifiles import *
import time

def getNotesFromDirection(directions, msg):
    messages = []
    for i in directions:
        new_note = ((msg.note + (i * 12)) % 128)
        messages.append(Message(msg.type, note=new_note,velocity=msg.velocity, time=0))

    return messages

def together(file_name, directions):
    last_note = int(round(time.time() * 1000))
    mido.get_output_names()
    port_name = mido.get_input_names()[0]
    print('Starting on port: ' + port_name)
    with MidiFile() as mid:
        track = MidiTrack()
        try:
            print("Waiting For Keyboard Input ... ")
            with mido.open_input() as inport:
                for msg in inport:
                    now = int(round(time.time() * 1000))
                    msg.time = now - last_note
                    last_note = now
                    if hasattr(msg, 'velocity') and msg.velocity == 0:
                        msg = Message('note_off', note=msg.note, velocity=msg.velocity, time=msg.time)
                    print(msg)
                    track.append(msg)
                    if hasattr(msg, 'note'):
                        for m in getNotesFromDirection(directions,msg):
                            track.append(m)
                            print(m)
                    print()
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
# together("new_song.mid",[1,10,7])
# from midi.lib import playMidiFile
#
# playMidiFile.play_music("new_song.mid")
