# Dependacies
There are new dependancies being the use of `mido` package for dealing with midi files and pygames for playing the
midi files through python.

## Instilation

### mido
```
pip3 install mido
pip3 install --pre python-rtmidi
```

### pygames
````
pip3 install pygame
````

# How to run these files

## Everything should be done in test.py
This is where you can call your functions from each of the file folders where the documentation for them is in.

## You should not be calling classes in the lib folder
At the base of each folder such as `calculation` folder there is a script that handles all the overhead and requiring what you need.
if for some reason you want to use the actual script in lib, for reasons of memory or anything else then it is your responsibility to
enter the proper information.

midiutil docs: `http://www.emergentmusics.org/midiutil`
mido Docs: `https://mido.readthedocs.org/en/latest/`
