__author__ = 'shawn'

import pygame

def play_music(music_file):
    freq = 44100    # audio CD quality=
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    try:
        pygame.mixer.music.set_volume(0.8)
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print ("\nMusic file %s loaded!" % music_file)
        except pygame.error:
            print ("File %s not found! (%s)" % (music_file, pygame.get_error()) )
            return
        pygame.mixer.music.play()
        print("\nPlaying Music ... ")
        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)
        print("Done playing!")
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit