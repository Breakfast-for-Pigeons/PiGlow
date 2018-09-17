#!/usr/bin/python3
"""
Swirling Vortex

This program lights up the LEDs one at at time then
then fades them on all 3 arms at the same time.

....................

Functions:
- swirling_vortex: Lights up 1 color at a time, Fades colors

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
SLEEP_SPEED = 0.01

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
            swirling_vortex()
            sleep(1)
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def swirling_vortex():
    """
    Lights up 1 color at a time, Fades colors
    """
    # Turn on red
    PYGLOW.color("red", 60)
    sleep(SLEEP_SPEED)
    # Turn on orange
    PYGLOW.color("orange", 60)
    sleep(SLEEP_SPEED)
    # Fade red
    PYGLOW.color("red", 50)
    sleep(SLEEP_SPEED)
    # Turn on yellow
    PYGLOW.color("yellow", 60)
    sleep(SLEEP_SPEED)
    # Fade red and orange
    PYGLOW.color("red", 40)
    sleep(SLEEP_SPEED)
    PYGLOW.color("orange", 50)
    sleep(SLEEP_SPEED)
    # Turn on green
    PYGLOW.color("green", 60)
    sleep(SLEEP_SPEED)
    # Fade red, orange, and yellow
    PYGLOW.color("red", 30)
    sleep(SLEEP_SPEED)
    PYGLOW.color("orange", 40)
    sleep(SLEEP_SPEED)
    PYGLOW.color("yellow", 50)
    sleep(SLEEP_SPEED)
    # Turn on blue
    PYGLOW.color("blue", 60)
    sleep(SLEEP_SPEED)
    # Fade red, orange, yellow, green
    PYGLOW.color("red", 20)
    sleep(SLEEP_SPEED)
    PYGLOW.color("orange", 30)
    sleep(SLEEP_SPEED)
    PYGLOW.color("yellow", 40)
    sleep(SLEEP_SPEED)
    PYGLOW.color("green", 50)
    sleep(SLEEP_SPEED)
    # Turn on white
    PYGLOW.color("white", 60)
    sleep(SLEEP_SPEED)
    # Fade red, orange, yellow, green, and blue
    PYGLOW.color("red", 10)
    sleep(SLEEP_SPEED)
    PYGLOW.color("orange", 20)
    sleep(SLEEP_SPEED)
    PYGLOW.color("yellow", 30)
    sleep(SLEEP_SPEED)
    PYGLOW.color("green", 40)
    sleep(SLEEP_SPEED)
    PYGLOW.color("blue", 50)
    sleep(SLEEP_SPEED)
    # Fade all
    PYGLOW.color("red", 0)
    sleep(SLEEP_SPEED)
    PYGLOW.color("orange", 10)
    sleep(SLEEP_SPEED)
    PYGLOW.color("yellow", 20)
    sleep(SLEEP_SPEED)
    PYGLOW.color("green", 30)
    sleep(SLEEP_SPEED)
    PYGLOW.color("blue", 40)
    sleep(SLEEP_SPEED)
    PYGLOW.color("white", 50)
    sleep(SLEEP_SPEED)
    # Fade orange, yellow, green, blue, and white
    PYGLOW.color("orange", 0)
    sleep(SLEEP_SPEED)
    PYGLOW.color("yellow", 10)
    sleep(SLEEP_SPEED)
    PYGLOW.color("green", 20)
    sleep(SLEEP_SPEED)
    PYGLOW.color("blue", 30)
    sleep(SLEEP_SPEED)
    PYGLOW.color("white", 40)
    sleep(SLEEP_SPEED)
    # Fade yellow, green, blue, and white
    PYGLOW.color("yellow", 0)
    sleep(SLEEP_SPEED)
    PYGLOW.color("green", 10)
    sleep(SLEEP_SPEED)
    PYGLOW.color("blue", 20)
    sleep(SLEEP_SPEED)
    PYGLOW.color("white", 30)
    sleep(SLEEP_SPEED)
    # Fade green, blue, and white
    PYGLOW.color("green", 0)
    sleep(SLEEP_SPEED)
    PYGLOW.color("blue", 10)
    sleep(SLEEP_SPEED)
    PYGLOW.color("white", 20)
    sleep(SLEEP_SPEED)
    # Fade blue, and white
    PYGLOW.color("blue", 0)
    sleep(SLEEP_SPEED)
    PYGLOW.color("white", 10)
    sleep(SLEEP_SPEED)
    # Fade white
    PYGLOW.color("white", 0)
    sleep(SLEEP_SPEED)


if __name__ == '__main__':
    main()
