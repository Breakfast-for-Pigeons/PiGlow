################################################################
#                        Fading Snakes                         #
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

def snake_12():
    pyglow.set_leds(snake_12_leds, 100)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 90)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 80)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 70)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 60)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 50)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 40)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 30)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 20)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 10)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_12_leds, 0)
    pyglow.update_leds()
    sleep(0.1)

def snake_13():
    pyglow.set_leds(snake_13_leds, 100)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 90)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 80)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 70)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 60)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 50)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 40)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 30)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 20)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 10)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_13_leds, 0)
    pyglow.update_leds()
    sleep(0.1)
    
def snake_23():
    pyglow.set_leds(snake_23_leds, 100)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 90)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 80)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 70)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 60)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 50)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 40)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 30)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 20)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 10)
    pyglow.update_leds()
    sleep(0.1)
    pyglow.set_leds(snake_23_leds, 0)
    pyglow.update_leds()
    sleep(0.1)

while True:
    snake_12()
    sleep(sleep_speed)
    snake_23()
    sleep(sleep_speed)
    snake_13()
    sleep(sleep_speed)
