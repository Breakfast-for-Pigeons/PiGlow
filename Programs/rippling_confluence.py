#!/usr/bin/python3
"""
Rippling Confluence

This program is basically my "Light the Fuse" program in
reverse. It lights up 2 arms at once and converges into the
third arm. It also creates "ripples" by dimming the brightness of
the LEDs one at a time.

....................

Functions:

- confluence_slow: Controls which fuse to light
- confluence_fast: Lights up arm 1, then 2 and 3
- confluence_1_and_2_into_3: Lights up arms 1 and 2, then arm 3
- confluence_1_and_3_into_2: Lights up arms 1 and 3, then arm 2
- confluence_2_and_3_into_1: Lights up arms 2 and 3, then arm 1
- rippling_confluence_1: Ripples the lights on arms 1 and 2, then arm 3
- rippling_confluence_2: Ripples the lights on arms 1 and 3, then arm 2
- rippling_confluence_3: Ripples the lights on arms 2 and 3, then arm 1

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
            confluence_slow()
            confluence_fast()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def confluence_2_and_3_into_1(sleep_speed):
    """
    Lights up arms 2 and 3, then arm 1
    """
    # Uncomment the following line for testing/debugging
    # print("Confluence 2 and 3 into 1...")

    sleep_speed = sleep_speed
    counter = 10

    # Arm 2 and 3, Red
    PYGLOW.led(7, 120)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 120)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9,  120)
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 120)
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 120)
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 120)
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 1, White
    PYGLOW.led(6, 120)
    sleep(sleep_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 120)
    sleep(sleep_speed)
    # Arm 1, Green
    PYGLOW.led(4, 120)
    sleep(sleep_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 120)
    sleep(sleep_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 120)
    sleep(sleep_speed)
    # Arm 1, Red
    PYGLOW.led(1, 120)
    sleep(sleep_speed)
    while counter > 0:
        rippling_confluence_1(sleep_speed)
        counter -= 1
    # Turn 'em off one at a time
    # Arm 2 and 3, Red
    PYGLOW.led(7, 0)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 0)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 0)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 0)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 0)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 0)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Arm 1, White
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    # Arm 1, Green
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    # Arm 1, Red
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    # Pause before next function
    sleep(1)


def confluence_1_and_3_into_2(sleep_speed):
    """
    Lights up arms 1 and 3, then arm 2
    """
    # Uncomment the following line for testing/debugging
    # print("Confluence 1 and 3 into 2...")

    sleep_speed = sleep_speed
    counter = 10

    # Arm 1 and 3, Red
    PYGLOW.led(1, 120)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 120)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 120)
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 120)
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 120)
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 120)
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 120)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 120)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 120)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 120)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 120)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, 120)
    sleep(sleep_speed)
    while counter > 0:
        rippling_confluence_2(sleep_speed)
        counter -= 1
    # Arm 1 and 3, Red
    PYGLOW.led(1, 0)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 0)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 0)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 0)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 0)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 0)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    sleep(1)


def confluence_1_and_2_into_3(sleep_speed):
    """
    Lights up arms 1 and 2, then arm 3
    """
    # Uncomment the following line for testing/debugging
    # print("Confluence 1 and 2 into 3...")

    sleep_speed = sleep_speed
    counter = 10

    # Arm 1 and 2, Red
    PYGLOW.led(1, 120)
    PYGLOW.led(7, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 120)
    PYGLOW.led(8, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 120)
    PYGLOW.led(9, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 120)
    PYGLOW.led(10, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 120)
    PYGLOW.led(11, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 120)
    PYGLOW.led(12, 120)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    while counter > 0:
        rippling_confluence_3(sleep_speed)
        counter -= 1
    # Arm 1 and 2, Red
    PYGLOW.led(1, 0)
    PYGLOW.led(7, 0)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 0)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 0)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 0)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 0)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 0)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    sleep(1)


def rippling_confluence_1(sleep_speed):
    """
    Ripples the lights on arms 1 and 2, then arm 3
    """
    # Uncomment the following line for testing/debugging
    # print("ripple speed is:", ripple_speed)

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    # Ripple
    # Arm 2 and 3, Red
    PYGLOW.led(7, 60)
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    # Arm 2 and 3, Red
    PYGLOW.led(7, 120)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 60)
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(8, 120)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 60)
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(9, 120)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 60)
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(10, 120)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 60)
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(11, 120)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 60)
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(12, 120)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 1, White
    PYGLOW.led(6, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    sleep(ripple_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    sleep(ripple_speed)
    # Arm 1, Green
    PYGLOW.led(4, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    sleep(ripple_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    sleep(ripple_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 80)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    sleep(ripple_speed)
    # Arm 1, Red
    PYGLOW.led(1, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    sleep(ripple_speed)


def rippling_confluence_2(sleep_speed):
    """
    Ripples the lights on arms 1 and 3, then arm 2
    """
    # Uncomment the following line for testing/debugging
    # print("ripple speed is:", ripple_speed)

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    # Ripple
    # Arm 1 and 3, Red
    PYGLOW.led(1, 60)
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 60)
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 60)
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 60)
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 60)
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 60)
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 2, White
    PYGLOW.led(12, 60)
    sleep(ripple_speed)
    PYGLOW.led(12, 120)
    sleep(ripple_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 60)
    sleep(ripple_speed)
    PYGLOW.led(11, 120)
    sleep(ripple_speed)
    # Arm 2, Green
    PYGLOW.led(10, 60)
    sleep(ripple_speed)
    PYGLOW.led(10, 120)
    sleep(ripple_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 60)
    sleep(ripple_speed)
    PYGLOW.led(9, 120)
    sleep(ripple_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 60)
    sleep(ripple_speed)
    PYGLOW.led(8, 120)
    sleep(ripple_speed)
    # Arm 2, Red
    PYGLOW.led(7, 60)
    sleep(ripple_speed)
    PYGLOW.led(7, 120)
    sleep(ripple_speed)


def rippling_confluence_3(sleep_speed):
    """
    Ripples the lights on arms 2 and 3, then arm 1
    """
    # Uncomment the following line for testing/debugging
    # print("ripple speed is:", ripple_speed)

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    # Ripple
    # Arm 1 and 2, Red
    PYGLOW.led(1, 60)
    PYGLOW.led(7, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    PYGLOW.led(7, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 60)
    PYGLOW.led(8, 60)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    PYGLOW.led(8, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 60)
    PYGLOW.led(9, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    PYGLOW.led(9, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 60)
    PYGLOW.led(10, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    PYGLOW.led(10, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 60)
    PYGLOW.led(11, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    PYGLOW.led(11, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 60)
    PYGLOW.led(12, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    PYGLOW.led(12, 120)
    sleep(ripple_speed)
    # Arm 3, White
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 3, Green
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 3, Red
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)


def confluence_slow():
    """
    Gradually increases the speed at which the LEDs light up
    """
    # Uncomment the following lines for testing/debugging
    # print("Confluence")
    # print("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def confluence_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    # Uncomment the following line for testing/debugging
    # print("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        # Uncomment the following line for testing/debugging
        # print("sleep_speed = ", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025


if __name__ == '__main__':
    main()
