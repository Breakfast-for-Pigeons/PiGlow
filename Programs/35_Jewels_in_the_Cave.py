################################################################
#                    Jewels in the Cave                        #
################################################################
# Description:                                                 #
# This program randomly turns on an LED, and then randomly     #
# turns one on off. At a brightness setting of 1, the LEDs     #
# look like jewels.                                            #
#                                                              #
# List of jewels:                                              #
# Red = Ruby                                                   #
# Orange = Citrine                                             #
# Yellow = Beryl                                               #
# Green = Emerald                                              #
# Blue = Sapphire                                              #
# White = Diamond                                              #
#                                                              #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep
import random

pyglow = PyGlow()

# Initialize
pyglow.all(0)

# Variables
sleep_speed = 0.5
brightness = 1

# List of leds
list_of_leds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def jewels_in_the_cave():
    sleep(sleep_speed)
    # Turn on a random led
    random_led = int(random.choice(list_of_leds))
    pyglow.led(random_led, brightness)
    sleep(sleep_speed)
    # Turn off a random led
    random_led = int(random.choice(list_of_leds))
    pyglow.led(random_led, 0)
    sleep(sleep_speed)

# Start the Program
try:
    while True:
        jewels_in_the_cave()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
