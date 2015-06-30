# Games

## importing the functions
It is as simple as adding this line to your imports 
```
from games import play
```

## play_keep_up
This is a game in which you need to try and keep up with the keyboard as it moves faster and faster through notes.
### The optional parameters you can pass are:
#### 1. note_length
This is the initial lenght of time at which the notes will be changing at (In seconds)

#### 2. min_time
This is the bottom cap that the time between notes can get. (In seconds)
 
#### 3. inc
This is the time at which the note_length will be changing after every wrong note.

## play_octaves
This function plays the notes you play but with the higher octave at the same time.

### Required Parameters

#### 1. file_name
This is the name that the file will be saved to.

#### 2. directions
This is a list of values which are the octaves you wish to play at the same time, example: `[1,-1]` which is up 1 octave and down 1

### Optional Parameters

#### 1. play
A boolean which is default to false, if true then it will play the music after it saves

## play_to_continue
This is a game in which the notes are not changing, where they will only change once you have gotten the write note that
is displayed on the screen. This function takes no parameters.

