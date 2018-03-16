################################################################
#                       Pulsing Snakes                         #
################################################################
# Description:                                                 #
# The title explains it.                                       #
#                                                              #
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
def pulsing_snake_12():
    pulse_speed = 200
    while pulse_speed > 100:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.set_leds(snake_12_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed -= 1
    pyglow.set_leds(snake_12_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)

def pulsing_snake_13():
    pulse_speed = 200
    while pulse_speed > 100:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.set_leds(snake_13_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed -= 1
    pyglow.set_leds(snake_13_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)
    
def pulsing_snake_23():
    pulse_speed = 200
    while pulse_speed > 100:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.set_leds(snake_23_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed -= 1
    pyglow.set_leds(snake_23_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)

# Start the program
try:
    while True:
        # 12, 13, 23
        pulsing_snake_12()
        pulsing_snake_13()
        pulsing_snake_23()
        # 13, 23, 12
        pulsing_snake_13()
        pulsing_snake_23()
        pulsing_snake_12()
        # 23, 12, 13
        pulsing_snake_23()
        pulsing_snake_12()
        pulsing_snake_13()
        # 12, 23, 13
        pulsing_snake_12()
        pulsing_snake_23()
        pulsing_snake_13()
        # 23, 13, 12
        pulsing_snake_23()
        pulsing_snake_13()
        pulsing_snake_12()
        # 13, 12, 23
        pulsing_snake_13()
        pulsing_snake_12()
        pulsing_snake_23()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()