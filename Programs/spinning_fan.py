#!/usr/bin/python3
"""
Spinning Fan

This program lights up the individual arms one at at time,
and  then gradually increases the speed.  Then the program
starts over again.

....................

Functions:

- spinning_fan: Turns on one arm at a time.
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
            spinning_fan()
            go_fast()
            go_faster()
            go_really_fast()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def spinning_fan():
    """
    Turns on one arm at a time.
    """
    # Uncomment the following line for testing/debugging
    # print("Increasing speed...")

    sleep_speed = 0.5

    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
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
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
        # decrease counter
        sleep_speed -= 0.0025


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    # Uncomment the following line for testing/debugging
    # print("Going faster...")

    sleep_speed = 0.01
    counter = 50

    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
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
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
        # decrease counter
        counter -= 1
    sleep(2)


if __name__ == '__main__':
    main()
