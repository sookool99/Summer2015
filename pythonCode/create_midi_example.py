__author__ = 'shawn'
# Some 'docs' can be found here: http://www.emergentmusics.org/midiutil
from midiutil.MidiFile3 import MIDIFile

MyMIDI = MIDIFile(2)

# Tracks are numbered from zero. Times are measured in beats.
track = 0
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

# Add a note. addNote expects the following information:
track = 0
channel = 0
pitch = 60
time = 0
duration = 5
volume = 100

# Now add the note.
MyMIDI.addNote(track,channel,pitch,time,duration,volume)

track = 0
channel = 0
pitch = 60
time = 0
duration = 5
volume = 100

# Now add the note.
MyMIDI.addNote(0,0,61,5,5,100)

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()