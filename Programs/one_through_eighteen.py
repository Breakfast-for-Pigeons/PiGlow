#!/usr/bin/python3
"""
One Through Eighteen

This program lights up LEDs 1 through 18 one at at time and
gradually increases the speed.

....................

Functions:
- run_10_times: Cycles throught the LEDs 10 times
- increase_speed: Gradually increases the speed

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
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
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
        increase_speed()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def increase_speed():
    """
    Gradually increases the speed at which the LEDs light up
    """
    # Uncomment the following line for testing/debugging
    # print("Increasing speed...")
    led_number = 1
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        while led_number < 19:
            PYGLOW.led(led_number, 100)    # light up LED
            sleep(sleep_speed)
            PYGLOW.led(led_number, 0)      # turn off LED
            sleep(sleep_speed)
            led_number += 1
        led_number = 1                     # Reset LED number to 1
        sleep_speed -= 0.05                # Increase speed
    run_10_times()


def run_10_times():
    """ Run 10 times

    Once the program has reached the max set speed, it will cycle
    throught the LEDs 10 times.

    """
    # Uncomment the following line for testing/debugging
    # print("Running 10 times...")
    counter = 10
    while counter > 0:
        # Set (or Reset) led_number to 1
        led_number = 1
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        while led_number < 19:
            PYGLOW.led(led_number, 100)    # light up LED
            sleep(0.05)
            PYGLOW.led(led_number, 0)      # turn off LED
            sleep(0.05)
            led_number += 1                # increment LED number
        counter -= 1                       # decrease counter
    increase_speed()


if __name__ == '__main__':
    main()
