__author__ = 'shawn'
import pygame, sys
import time
from random import randint
import mido

last_note_played = time.time()
all_notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font = pygame.font.Font(None, 156)
text = font.render("Note: ", True, (0, 128, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    if time.time() - last_note_played > 1:
        last_note_played = time.time()
        text = font.render("Note: " + all_notes[randint(0,len(all_notes) -1)] , True, (0, 128, 0))
    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
# screen.fill((255, 255, 255))
# screen.blit(text,
#     (320 - text.get_width() // 2, 240 - text.get_height() // 2))
#
# pygame.display.flip()
# port_name = mido.get_input_names()[0]
# mido.open_input()
# with mido.open_input(port_name) as inport:
#     print("outside")
#     while 1:
#         for msg in inport:
#             print("inside")
#             if hasattr(msg, 'note'):
#                 text = font.render("Note: " + str(msg.note) , True, (0, 128, 0))
#         screen.fill((255, 255, 255))
#         screen.blit(text,
#             (320 - text.get_width() // 2, 240 - text.get_height() // 2))
#
#         pygame.display.flip()
#         clock.tick(60)