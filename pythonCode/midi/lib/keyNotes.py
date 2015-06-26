__author__ = 'shawn'


all_notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def get_all_key_notes():
    return get_all_in_range(0,128)

def get_notes():
    return get_all_in_range(60,73)



def get_all_in_range(start, end):
    notes = {}
    for i in range(start,end):
        notes[i] = all_notes[i % len(all_notes)]
    return notes
