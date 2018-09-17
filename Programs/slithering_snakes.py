#!/usr/bin/python3
"""
Slithering Snakes

I think the title is self explanatory.

....................

Functions:
- slithering_snake_12: Lights up then turns off the LEDs on arms 1 and 2
- slithering_snake_13: Lights up then turns off the LEDs on arms 1 and 3
- slithering_snake_21: Lights up then turns off the LEDs on arms 2 and 1
- slithering_snake_23: Lights up then turns off the LEDs on arms 2 and 3
- slithering_snake_31: Lights up then turns off the LEDs on arms 3 and 1
- slithering_snake_32: Lights up then turns off the LEDs on arms 3 and 2

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
SLEEP_SPEED = 0.10

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
            # Snakes 12, 13, 21, 23, 31, 32
            slithering_snake_12()
            sleep(1)
            slithering_snake_13()
            sleep(1)
            slithering_snake_21()
            sleep(1)
            slithering_snake_23()
            sleep(1)
            slithering_snake_31()
            sleep(1)
            slithering_snake_32()
            sleep(1)
            # Snakes 12, 23, 31, 13, 32, 21
            slithering_snake_12()
            sleep(1)
            slithering_snake_23()
            sleep(1)
            slithering_snake_31()
            sleep(1)
            slithering_snake_13()
            sleep(1)
            slithering_snake_32()
            sleep(1)
            slithering_snake_21()
            sleep(1)
            # Snakes 13, 12, 23, 21, 31, 32
            slithering_snake_13()
            sleep(1)
            slithering_snake_12()
            sleep(1)
            slithering_snake_23()
            sleep(1)
            slithering_snake_21()
            sleep(1)
            slithering_snake_31()
            sleep(1)
            slithering_snake_32()
            sleep(1)
            # Snakes 13, 32, 21, 12, 23, 31
            slithering_snake_13()
            sleep(1)
            slithering_snake_32()
            sleep(1)
            slithering_snake_21()
            sleep(1)
            slithering_snake_12()
            sleep(1)
            slithering_snake_23()
            sleep(1)
            slithering_snake_31()
            sleep(1)
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def slithering_snake_12():
    """
    Lights up then turns off the LEDs on arms 1 and 2
    """
    # Light up Snake 12
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 12
    PYGLOW.led(1, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 0)
    sleep(SLEEP_SPEED)


def slithering_snake_13():
    """
    Lights up then turns off the LEDs on arms 1 and 3
    """
    # Light up Snake 13
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 13
    PYGLOW.led(1, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 0)
    sleep(SLEEP_SPEED)


def slithering_snake_21():
    """
    Lights up then turns off the LEDs on arms 2 and 1
    """
    # Light up Snake 21
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 21
    PYGLOW.led(7, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 0)
    sleep(SLEEP_SPEED)


def slithering_snake_23():
    """
    Lights up then turns off the LEDs on arms 2 and 3
    """
    # Light up Snake 23
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 23
    PYGLOW.led(7, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 0)
    sleep(SLEEP_SPEED)


def slithering_snake_31():
    """
    Lights up then turns off the LEDs on arms 3 and 1
    """
    # Light up Snake 31
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 31
    PYGLOW.led(13, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 0)
    sleep(SLEEP_SPEED)


def slithering_snake_32():
    """
    Lights up then turns off the LEDs on arms 3 and 2
    """
    # Light up Snake 32
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    # Turn off Snake 32
    PYGLOW.led(13, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 0)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 0)
    sleep(SLEEP_SPEED)


if __name__ == '__main__':
    main()
