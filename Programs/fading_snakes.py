#!/usr/bin/python3
"""
Fading Snakes (or should the title be: Fading Pythons)

I think the title is self explanatory.

....................

Functions:
- fading_snake_12: Lights up the LEDs on arms 1 and 2 and fades them
- fading_snake_13: Lights up the LEDs on arms 1 and 3 and fades them
- fading_snake_23: Lights up the LEDs on arms 2 and 3 and fades them

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
SLEEP_SPEED = 1

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
            fading_snake_12()
            sleep(SLEEP_SPEED)
            fading_snake_23()
            sleep(SLEEP_SPEED)
            fading_snake_13()
            sleep(SLEEP_SPEED)
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def fading_snake_12():
    """
    Lights up the LEDs on arms 1 and 2 and fades them
    """
    PYGLOW.set_leds(SNAKE_12_LEDS, 100)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 90)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 80)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 70)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 60)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 50)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 40)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 30)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 20)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 10)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_12_LEDS, 0)
    PYGLOW.update_leds()
    sleep(0.1)


def fading_snake_13():
    """
    Lights up the LEDs on arms 1 and 3 and fades them
    """
    PYGLOW.set_leds(SNAKE_13_LEDS, 100)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 90)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 80)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 70)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 60)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 50)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 40)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 30)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 20)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 10)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_13_LEDS, 0)
    PYGLOW.update_leds()
    sleep(0.1)


def fading_snake_23():
    """
    Lights up the LEDs on arms 2 and 3 and fades them
    """
    PYGLOW.set_leds(SNAKE_23_LEDS, 100)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 90)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 80)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 70)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 60)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 50)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 40)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 30)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 20)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 10)
    PYGLOW.update_leds()
    sleep(0.1)
    PYGLOW.set_leds(SNAKE_23_LEDS, 0)
    PYGLOW.update_leds()
    sleep(0.1)


if __name__ == '__main__':
    main()
