
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))
import pygame
from pygame.locals import *

import psmove
import time
import math
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
step_m = 0.1
step = 0.1
changeU = False
changeD = False
changeK = True
mode = '0'
while not done:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
       if (event.type == KEYUP) or (event.type == KEYDOWN):
          print event
          if (event.key == K_ESCAPE):
             done = True
          if (event.key == K_0):
             mode = '0'
             r2 = r
             g2 = g
             b2 = b
          if (event.key == K_r):
             mode = 'r'
          if (event.key == K_g):
             mode = 'g'
          if (event.key == K_b):
             mode = 'b'
          if (event.key == K_k):
             mode = 'k'
             changeK = True
          if (event.key == K_u):
             r = 255
             g = 0
             b = 0
          if (event.key == K_i):
             r = 255
             g = 255
             b = 255
          if (event.key == K_o):
             r = 0
             g = 0
             b = 0
    if m1.poll():
        if key[K_j]:
            if step - 0.1 >= 0.0: step = step - 0.1
        if key[K_l]:
            if step + 0.1 <= 1.0: step = step + 0.1


        if mode == '0':

            if key[K_1]:
                if r + step_m > r2: r = r2
                else: r = int(float(r) + step_m)
                if g + step_m > g2: g = g2
                else: g = int(float(g) + step_m)
                if b + step_m > b2: b = b2
                else: b = int(float(b) + step_m)
            
            if key[K_2]:
                if r - step_m < 0: r = 0
                else: r = int(float(r) - step_m)
                if g - step_m < 0: g = 0
                else: g = int(float(g) - step_m)
                if b - step_m < 0: b = 0
                else: b = int(float(b) - step_m)
        
        if mode == 'r':

            if key[K_1]:
                if r + step_m > r2: r = r2
                else: r = int(float(r) + step_m)
            
            if key[K_2]:
                if r - step_m < 0: r = 0
                else: r = int(float(r) - step_m)
        
        if mode == 'g':

            if key[K_1]:
                if g + step_m > g2: g = g2
                else: g = int(float(g) + step_m)
            
            if key[K_2]:
                if g - step_m < 0: g = 0
                else: g = int(float(g) - step_m)
        
        if mode == 'b':

            if key[K_1]:
                if b + step_m > b2: b = b2
                else: b = int(float(b) + step_m)
            
            if key[K_2]:
                if b - step_m < 0: b = 0
                else: b = int(float(b) - step_m)
        
        if mode == 'k':
            if changeK:
                if r + step*r2 > r2: r = r2
                else: r = int(float(r) + step*r2)
                if g + step*g2 > g2: g = g2
                else: g = int(float(g) + step*g2)
                if b + step*b2 > b2: b = b2
                else: b = int(float(b) + step*b2)
                if r == r2 and g == g2 and b == b2: changeK = False
            else:
                if r - step*r2 < 0: r = 0
                else: r = int(float(r) - step*r2)
                if g - step*g2 < 0: g = 0
                else: g = int(float(g) - step*g2)
                if b - step*b2 < 0: b = 0
                else: b = int(float(b) - step*b2)
                if r == 0 and g == 0 and b == 0: changeK = True
        
            

        if key[K_x]:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)


	    buttons = m1.get_buttons()
	    if buttons & psmove.Btn_TRIANGLE:
	      print 'triangle pressed'
              rumble = not rumble
              time.sleep(.2)

	    if rumble:
	      m1.set_rumble(255)
            else:
	      m1.set_rumble(0)
	    
		    
    m1.set_leds(r, g, b)
#    time.sleep(.2)
    m1.update_leds()




