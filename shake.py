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
step_m = 0.000003
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
r2 = r
g2 = g
b2 = b
last = 0

rf = float(r);
gf = float(g);
bf = float(b);

while True:
    if move.poll():
        
        #print move.gz

        if (abs(move.gz) > 6000):	
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		r2 = r
		g2 = g
		b2 = b
		rf = float(r)
		gf = float(g)
		bf = float(b)

	if True:
		if (rf - step_m) < 0.0: rf = 0.0
		else: rf = rf - step_m*float(r2)
                if (gf - step_m) < 0.0: gf = 0.0
                else: gf = gf - step_m*float(g2)
                if (bf - step_m) < 0.0: bf = 0.0
                else: bf = bf - step_m*float(b2)

		r = int(rf)
		g = int(gf)
		b = int(bf)
		
	
        #print 'y:', move.gy
        #print 'z:', move.gz
	#print rf, r

	move.set_leds(r, g, b)
        move.update_leds()
		
	#time.sleep(0.2)
