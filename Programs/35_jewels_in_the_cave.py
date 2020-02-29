#!/usr/bin/env python3
"""
Jewels in the Cave

This program randomly turns on an LED, and then randomly turns one
on and off. At a brightness setting of 1, the LEDs look like jewels.

List of jewels:
    Red = Ruby
    Orange = Citrine
    Yellow = Beryl
    Green = Emerald
    Blue = Sapphire
    White = Diamond

....................

Functions:
- jewels_in_the_cave: Randomly turns on and off an LED

....................

Requirements:
    PyGlow.py (many thanks to benleb for this program)
    bfp_piglow_modules.py

You will have these files if you downloaded the entire repository.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import random
from time import sleep
from PyGlow import PyGlow
from bfp_piglow_modules import print_header
from bfp_piglow_modules import check_log_directory
from bfp_piglow_modules import stop

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

SLEEP_SPEED = 0.10

########################################################################
#                            Functions                                 #
########################################################################


def jewels_in_the_cave():
    """
    Randomly turns on and off an LED
    """

    sleep_speed = 0.5
    brightness = 1
    list_of_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    10, 11, 12, 13, 14, 15, 16, 17, 18]

    sleep(sleep_speed)
    # Turn on a random led
    random_led = int(random.choice(list_of_leds))
    PYGLOW.led(random_led, brightness)
    sleep(sleep_speed)
    # Turn off a random led
    random_led = int(random.choice(list_of_leds))
    PYGLOW.led(random_led, 0)
    sleep(sleep_speed)


def main():
    """ The main fuction """

    while True:
        jewels_in_the_cave()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Print header
        print_header()
        # STEP03: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP04: Run the main function
        main()
    except KeyboardInterrupt:
        stop()
