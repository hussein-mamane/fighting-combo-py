import pygame
from datetime import datetime
import sys
from pygame.locals import *
from enum import Enum
from attacks import *

FPS=60
FRAME_TIME = round((1/FPS),4)*1000 # milliseconds/frame

a = datetime.now()

class State(str,Enum):
     IDLE = 0
     COMBO = 1

     

CLOCK = pygame.time.Clock()


pygame.init()
game_shoud_run = True
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Combo")

input_buffer = InputBuffer()
combo_handler = ComboHandler()

state = State.IDLE
while game_shoud_run:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
                game_shoud_run = False
        if event.type == KEYDOWN:
            if state == State.IDLE:
                if event.key == K_s:
                     pass
                if event.key == K_d:
                     pass
            if state == State.COMBO:
                if event.key == K_s:
                     pass
                if event.key == K_d:
                     pass 
        if event.type == KEYUP:
            if state == State.IDLE:
                if event.key == K_s:
                     pass
                if event.key == K_d:
                     pass
            if state == State.COMBO:
                if event.key == K_s:
                     pass
                if event.key == K_d:
                     pass    

pygame.quit()

b = datetime.now()
c=b-a
print(c.microseconds/1000)
sys.exit()
