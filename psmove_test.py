import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))

import psmove
import time
import math
import random

move = psmove.PSMove()

if move.connection_type == psmove.Conn_Bluetooth:
    print 'bluetooth'
elif move.connection_type == psmove.Conn_USB:
    print 'usb'
else:
    print 'unknown'

color_switch = True
step_m = 1
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
r2 = r
g2 = g
b2 = b

while True:
    if move.poll():

        print 'gyro:', (move.ax, move.ay, move.az)
	
	if ( float(move.ax) > -4501.0 and move.ax < 300):
                r = round(float(move.ax + 4600)/4800.0 * r2)              
                g = round(float(move.ax + 4600)/4800.0 * g2)               
                b = round(float(move.ax + 4600)/4800.0 * b2)               
		if r > r2: r = r2
		if g > g2: g = g2
		if b > b2: b = b2
		move.set_leds(int(r), int(g), int(b))
        	move.update_leds()
        elif (move.ax > -4600 and move.ax < -4500):
		move.set_leds(0, 0, 0)
        	move.update_leds()
	
        #if ( float(move.ax) > -4200.0 and move.ax < 300):
        #        r = round(float(move.ax + 4600)/4800.0 * 255)                 
	#	if r > 255: r = 255
	#	move.set_leds(int(r), 0, 0)
        #	move.update_leds()
        #elif (move.ax > 4070):
	#	move.set_leds(0, 0, 0)
        #	move.update_leds()

	if ( move.az > -100.0 and color_switch):
		color_switch = False
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		r2 = r
		g2 = g
		b2 = b
		move.set_leds(r, g, b)
        	move.update_leds()
	elif (move.az < -4450):
		color_switch = True        
		
	#time.sleep(0.2)
