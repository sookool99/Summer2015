# Midi file data

## importing the functions
It is as simple as adding this line to your imports 
```
from midi import logic
```

## Playing Midi File.
This function will read and play a midi file without any external resources needed.

### Examples
As simple as  `logic.play_file(myFileName)`

## start_keyboard_stream
This function with must have a midi port open (That is have a midi device plugged in) and it will take all keys press "live" 
from that device and display them and save to file.

NOTE: Currently to stop this from running you must cause a KeyboardInterrupt exception, which all that is, is killing the program from runnig.
Two ways to do this (in pycharm) is either by pressing "fn + command + f2" at the same time, or go into top menu bar and go to
Run->Stop

### Examples
`logic.start_keyboard_stream()` which will not save anything just print all output to the screen, to save just pass a file_name
`logic.start_keyboard_stream(myFileName)`


## Save and play
This is just an easy wrapper around the first two functions, which will do everything `start_keyboard_stream()` will do
and then after will play the file for you.

### Examples
`logic.save_and_play()` for default `new_song.mid` file or you can pass a file `logic.save_and_play(myFileName)`


## create_file_from_list
REQUIRMENT: must have list of `mido.midifiles.Message`

Creates a new midi file from a list of Messages objects. 

## Examples 
```
from mido.midifiles import Message
tmp = [Message('note_on', note=60, velocity=50, time=0), Message('note_off', note=60, velocity=124, time=5000)]

logic.create_file_from_list(tmp,"test123.mid")

logic.play_file("test123.mid")
```

## get_notes and get_all_notes
This function will return for you a dict mapping notes/key values (integer numbers) to their corresponding letters.

Just call the function like `allNotes = logic.get_all_notes()` or `smallKeyboardMidiOctaveNotes = logic.get_notes()`

If needed, because your keyboard has a different midi range being able to play then you can specify a different range of notes.