#!/usr/bin/python3
"""
Vib G. Roy

This program lights up like colors one at the same,
all white, all blue, etc... then gradually increases the
speed and then goes through the entire process again.

....................

Functions:

- vig_g_roy: Controls which fuse to light
- increase_speed: Gradually increases the speed
- go_fast: Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
- go_faster: Sleep_speed  is 0.01. Cycle through the LEDS 20 times
- go_really_fast: Sleep_speed is 0. Cycle through the LEDS 100 times

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

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW.all(0)

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
            increase_speed()
            go_fast()
            go_faster()
            go_really_fast()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def vib_g_yor(sleep_speed):
    """
    Cylces through all the colors
    """
    PYGLOW.color("white", 100)
    sleep(sleep_speed)
    PYGLOW.color("white", 0)
    PYGLOW.color("blue", 100)
    sleep(sleep_speed)
    PYGLOW.color("blue", 0)
    PYGLOW.color("green", 100)
    sleep(sleep_speed)
    PYGLOW.color("green", 0)
    PYGLOW.color("yellow", 100)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 0)
    PYGLOW.color("orange", 100)
    sleep(sleep_speed)
    PYGLOW.color("orange", 0)
    PYGLOW.color("red", 100)
    sleep(sleep_speed)
    PYGLOW.color("red", 0)


def increase_speed():
    """
    Gradually increases the speed at which the LEDs light up
    """
    # Uncomment the following line for testing/debugging
    # print("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        vib_g_yor(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def go_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    # Uncomment the following line for testing/debugging
    # print("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        vib_g_yor(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    # Uncomment the following line for testing/debugging
    # print("Going faster...")

    sleep_speed = 0.01
    counter = 20

    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        vib_g_yor(sleep_speed)
        # decrease counter
        counter -= 1


def go_really_fast():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    # Uncomment the following line for testing/debugging
    # print("Going really fast...")

    sleep_speed = 0
    counter = 100

    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        vib_g_yor(sleep_speed)
        # decrease counter
        counter -= 1
    sleep(2)


if __name__ == '__main__':
    main()
