__author__ = 'shawn'


all_notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def get_all_key_notes():
    return get_all_in_range(0,128)

def get_notes():
    return get_all_in_range(48,73)

def get_length_note():
    return len(all_notes)



def get_all_in_range(start, end):
    notes = {}
    for i in range(start,end):
        notes[i] = all_notes[i % len(all_notes)]
    return notes

def get_note_mapping(start, end):
    notes = {}
    for i in range(start, end):
        notes[i] = {"note":all_notes[i % len(all_notes)], "status":"note_off", "time_on":0, "last_duration":0}
    return notes

def get_all_note_mapping():
    return get_note_mapping(0,128)
