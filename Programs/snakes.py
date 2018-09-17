#!/usr/bin/python3
"""
Snakes (or should the title be: Pythons)

I think the title is self explanatory.

....................

Functions:
- snake_12: Lights up the LEDs on arms 1 and 2
- snake_13: Lights up the LEDs on arms 1 and 3
- snake_23: Lights up the LEDs on arms 2 and 3

....................

Requirements: PyGlow.py

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
from PyGlow import PyGlow

########################################################################
#                           Variables                                  #
########################################################################

PYGLOW = PyGlow()
SLEEP_SPEED = 2

########################################################################
#                            Lists                                     #
########################################################################

# Snake 12 LEDs (Same lights as Snake 21 - Since they are not slithering,
# the order doesn't matter)
SNAKE_12_LEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# Snake 13 LEDs (Same lights as Snake 31 - Since they are not slithering,
# the order doesn't matter)
SNAKE_13_LEDS = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# Snake 23 LEDs (Same lights as Snake 32 - Since they are not slithering,
# the order doesn't matter)
SNAKE_23_LEDS = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    The main function
    """
    print("Press Ctrl-C to stop the program.")
    try:
        while True:
            snake_12()
            snake_23()
            snake_13()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def snake_12():
    """
    Lights up the LEDs on arms 1 and 2
    """
    PYGLOW.set_leds(SNAKE_12_LEDS, 100)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)
    PYGLOW.set_leds(SNAKE_12_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


def snake_13():
    """
    Lights up the LEDs on arms 1 and 3
    """
    PYGLOW.set_leds(SNAKE_13_LEDS, 100)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)
    PYGLOW.set_leds(SNAKE_13_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


def snake_23():
    """
    Lights up the LEDs on arms 2 and 3
    """
    PYGLOW.set_leds(SNAKE_23_LEDS, 100)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)
    PYGLOW.set_leds(SNAKE_23_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


if __name__ == '__main__':
    main()
