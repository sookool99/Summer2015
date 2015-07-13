__author__ = 'shawn'
from games.lib import keep_up
from games.lib import symmetry
from games.lib import play_to_cont
from games.lib import training_program
from midi import logic

def play_keep_up(note_length=1, min_time=0.3, inc=0.01):
    game = keep_up.PlayToContinue()
    game.start(note_length, min_time, inc)

def play_octaves(file_name, directions, play=False):
    symmetry.together(file_name, directions)
    if play: logic.play_file(file_name)

def play_to_continue():
    game = play_to_cont.PlayToContinue()
    game.start()

def play_training_program(bpm = 60, note_file_name = 'testFile.txt', out_file_name = "new_song.mid"):
    training_program.PlayToContinue().start(bpm,note_file_name,out_file_name)
