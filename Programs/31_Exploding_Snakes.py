################################################################
#            Exploding Snakes a.k.a Exploding Pythons          #
################################################################
# Description:                                                 #
# The title pretty much explains it. The snakes start pulsing  #
# and eventually explode.                                      #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

# Initialize
pyglow.all(0)

# Variables
sleep_speed = 1

# Lists
# Snake 12 LEDs (Same lights as Snake 21 - Since they are not slithering, the order doesn't matter)
snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# Snake 13 LEDs (Same lights as Snake 31 - Since they are not slithering, the order doesn't matter)
snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# Snake 23 LEDs (Same lights as Snake 32 - Since they are not slithering, the order doesn't matter)
snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Functions
def exploding_snake_12():
    # Variables
    explode_speed = 0.020
    pulse_speed = 150
    # Pulse
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_12_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_12_leds, 100)
    sleep(1)
    # Explode Snake 12 
    ''' Uncomment the following print statement for feedback '''
    #print "Exploding Snake 12..."
    pyglow.led(6, 0)
    sleep(explode_speed)
    pyglow.led(18, 0)
    sleep(explode_speed)
    pyglow.led(11, 0)
    sleep(explode_speed)
    pyglow.led(5, 0)
    sleep(explode_speed)
    pyglow.led(10, 0)
    sleep(explode_speed)
    pyglow.led(4, 0)
    sleep(explode_speed)
    pyglow.led(9, 0)
    sleep(explode_speed)
    pyglow.led(3, 0)
    sleep(explode_speed)
    pyglow.led(8, 0)
    sleep(explode_speed)
    pyglow.led(2, 0)
    sleep(explode_speed)
    pyglow.led(7, 0)
    sleep(explode_speed)
    pyglow.led(1, 0)
    sleep(explode_speed)
    pyglow.update_leds()

    sleep(2)

def exploding_snake_13():
    # Variables
    explode_speed = 0.020
    pulse_speed = 150
    # Pulse
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_13_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_13_leds, 100)
    sleep(1)
    # Explode Snake 13 
    ''' Uncomment the following print statement for feedback '''
    #print "Exploding Snake 13..."
    pyglow.led(18, 0)
    sleep(explode_speed)
    pyglow.led(12, 0)
    sleep(explode_speed)
    pyglow.led(17, 0)
    sleep(explode_speed)
    pyglow.led(5, 0)
    sleep(explode_speed)
    pyglow.led(16, 0)
    sleep(explode_speed)
    pyglow.led(4, 0)
    sleep(explode_speed)
    pyglow.led(15, 0)
    sleep(explode_speed)
    pyglow.led(3, 0)
    sleep(explode_speed)
    pyglow.led(14, 0)
    sleep(explode_speed)
    pyglow.led(2, 0)
    sleep(explode_speed)
    pyglow.led(13, 0)
    sleep(explode_speed)
    pyglow.led(1, 0)
    sleep(explode_speed)
    pyglow.update_leds()

    sleep(2)
    
def exploding_snake_23():
    explode_speed = 0.020
    pulse_speed = 150
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_23_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_23_leds, 100)
    sleep(1)
    ''' Uncomment the following print statement for feedback '''
    #print "Exploding Snake 23..."
    # Explode Snake 13 
    pyglow.led(6, 0)
    sleep(explode_speed)
    pyglow.led(12, 0)
    sleep(explode_speed)
    pyglow.led(11, 0)
    sleep(explode_speed)
    pyglow.led(17, 0)
    sleep(explode_speed)
    pyglow.led(10, 0)
    sleep(explode_speed)
    pyglow.led(16, 0)
    sleep(explode_speed)
    pyglow.led(9, 0)
    sleep(explode_speed)
    pyglow.led(15, 0)
    sleep(explode_speed)
    pyglow.led(8, 0)
    sleep(explode_speed)
    pyglow.led(14, 0)
    sleep(explode_speed)
    pyglow.led(7, 0)
    sleep(explode_speed)
    pyglow.led(13, 0)
    sleep(explode_speed)
    pyglow.update_leds()

    sleep(2)

# Start the program
try:
    while True:
        # 12, 13, 23
        exploding_snake_12()
        exploding_snake_13()
        exploding_snake_23()
        # 13, 23, 12
        exploding_snake_13()
        exploding_snake_23()
        exploding_snake_12()
        # 23, 12, 13
        exploding_snake_23()
        exploding_snake_12()
        exploding_snake_13()
        # 12, 23, 13
        exploding_snake_12()
        exploding_snake_23()
        exploding_snake_13()
        # 23, 13, 12
        exploding_snake_23()
        exploding_snake_13()
        exploding_snake_12()
        # 13, 12, 23
        exploding_snake_13()
        exploding_snake_12()
        exploding_snake_23()
# Stop the program and turn off LEDs with Ctrl-C  
except KeyboardInterrupt:
    pyglow.all()
