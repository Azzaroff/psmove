
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))
import pygame
from pygame.locals import *

import time
import math
import psmove
import random

m1 = psmove.PSMove(0)
if psmove.psmove_count_connected() > 1: m2 = psmove.PSMove(1)

pygame.init()
screen = pygame.display.set_mode((1, 1))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
r2 = r
g2 = g
b2 = b
done = False
rumble = False
intensity = 1.0
while not done:
    for event in pygame.event.get():
       if (event.type == KEYUP) or (event.type == KEYDOWN):
          print event
          if (event.key == K_ESCAPE):
             done = True
          if (event.key == K_1):
             intensity = intensity - 0.1
             if intensity < 0: intensity = 0
	     elif intensity > 1: intensity = 1
    if m1.poll():
            r = int(float(r2)*float(intensity))
            g = int(float(g2)*float(ratio))
            b = int(float(b2)*float(ratio))
	    buttons = m1.get_buttons()
	    if buttons & psmove.Btn_TRIANGLE:
	      print 'triangle pressed'
              rumble = not rumble
              time.sleep(.2)

	    if rumble:
	      m1.set_rumble(255)
            else:
	      m1.set_rumble(0)
	    
		    
    m1.set_leds(255, 0, 0)
#    time.sleep(.2)
    m1.update_leds()




