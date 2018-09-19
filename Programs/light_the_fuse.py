#!/usr/bin/python3
"""
Light the Fuse

This program lights up arm 1, then lights up arms 2 and 3
at the same time. Then lights up arm 2, which then lights
up arms 1 and 3. Then lights up arm 3, which then lights
up arms 1 and 2.  Then goes through the whole thing again
while increasing the speed.

....................

Functions:

- light_the_fuse: Controls which fuse to light
- light_fuse_1: Lights up arm 1, then 2 and 3
- light_fuse_2: Lights up arm 2, then 1 and 3
- light_fuse_3: Lights up arm 3, then 1 and 2
- go_fast: Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
- go_faster: Sleep_speed  is 0.01. Cycle through the LEDS 20 times

....................

Requirements: PyGlow.py

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
#######################################################################
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
            light_the_fuse()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def light_fuse_1(sleep_speed):
    """
    Lights up the LEDs on arm 1 one at a time, then lights up the LEDs
    on both arm 2 and arm 3 one at a time.
    """
    # Arm 1, Red
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    # Arm 1, Green
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    # Arm 1, White
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 100)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 100)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 100)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 100)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 100)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    # Arm 2 and 3, Red
    PYGLOW.led(7, 100)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Turn 'em off
    PYGLOW.all(0)


def light_fuse_2(sleep_speed):
    """
    Lights up the LEDs on arm 2 one at a time, then lights up the LEDs
    on both arm 1 and arm 3 one at a time.
    """
    # Arm 2, Red
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 100)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 100)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 100)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 100)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 100)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    # Arm 1 and 3, Red
    PYGLOW.led(1, 100)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Turn 'em off
    PYGLOW.all(0)


def light_fuse_3(sleep_speed):
    """
    Lights up the LEDs on arm 2 one at a time, then lights up the LEDs
    on both arm 1 and arm 3 one at a time.
    """
    # Arm 3, Red
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 100)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 100)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 100)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 100)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 100)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    # Arm 1 and 2, Red
    PYGLOW.led(1, 100)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    # Turn 'em off
    PYGLOW.all(0)


def light_the_fuse():
    """
    Controls which fuse to light
    """

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    go_fast(sleep_speed)


def go_fast(sleep_speed):
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    # Uncomment the following line for testing/debugging
    # print("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        # Uncomment the following line for testing/debugging
        # print("sleep_speed = ", sleep_speed)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025
    go_faster()


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 10 times
    """
    # Uncomment the following line for testing/debugging
    # print("Going faster...")

    sleep_speed = 0.01
    counter = 10

    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("sleep_speed = ", sleep_speed)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # decrease counter
        counter -= 1
    sleep(2)


if __name__ == '__main__':
    main()
