################################################################
#                  Snakes  a.k.a.  Pythons                     #
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
sleep_speed = 2

# Lists
# Snake 12 LEDs (Same lights as Snake 21 - Since they are not slithering, the order doesn't matter)
snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# Snake 13 LEDs (Same lights as Snake 31 - Since they are not slithering, the order doesn't matter)
snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# Snake 23 LEDs (Same lights as Snake 32 - Since they are not slithering, the order doesn't matter)
snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Functions
def snake_12():
    pyglow.set_leds(snake_12_leds, 100)
    pyglow.update_leds()
    sleep(sleep_speed)
    pyglow.set_leds(snake_12_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)

def snake_13():
    pyglow.set_leds(snake_13_leds, 100)
    pyglow.update_leds()
    sleep(sleep_speed)
    pyglow.set_leds(snake_13_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)
    
def snake_23():
    pyglow.set_leds(snake_23_leds, 100)
    pyglow.update_leds()
    sleep(sleep_speed)
    pyglow.set_leds(snake_23_leds, 0)
    pyglow.update_leds()
    sleep(sleep_speed)

# Start the program
try:
    while True:
        snake_12()
        snake_23()
        snake_13()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()