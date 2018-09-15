#!/usr/bin/python3
"""
One Through Eighteen

This program lights up the LEDs on arm 1 one at at time,
then arm 2, then arm 3. Then turns off the lights one at a
time. Then increases the speed and goes through the entire
process again.

....................

Functions:
- turn_on_leds: Turns on the LEDs one at a time
- turn_off_leds: Turns off the LEDs one at a time
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
#                           Variables                                  #
########################################################################

PYGLOW = PyGlow()

# Feel free to modify the brightness setting below
LED_BRIGHTNESS = 100

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

    try:
        increase_speed()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        PYGLOW.all(0)


def turn_on_leds(sleep_speed):
    """
    Turns on the LEDs one at a time

    Arguments:
        sleep_speed
    """

    # Uncomment the following line for testing/debugging
    # print("Turning on LEDs...")
    led_number = 1
    # Uncomment the following line for testing/debugging
    # print("The current sleep speed (turn on LEDs) is:", sleep_speed)
    # Turn on LEDs one at a time
    while led_number < 19:
        PYGLOW.led(led_number, LED_BRIGHTNESS)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)


def turn_off_leds(sleep_speed):
    """
    Turns off the LEDs one at a time

    Arguments:
        sleep_speed
    """
    # Uncomment the following line for testing/debugging
    # print("Turning off LEDs...")

    # Set (or Reset) LED number
    led_number = 1

    # Turn off LEDs one at a time
    # print("The current sleep speed (turn off LEDs) is:", sleep_speed)

    # Turn off LEDs one at a time
    while led_number < 19:
        PYGLOW.led(led_number, 0)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)


def increase_speed():
    """
    Gradually increases the speed at which the LEDs light up
    """
    # Uncomment the following line for testing/debugging
    # print("Increasing speed...")
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print "The current speed is:", sleep_speed
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    run_10_times()


def run_10_times():
    """ Run 10 times

    Once the program was reached the max set speed, it will cycle
    throught the LEDs 10 times.

    """
    # Uncomment the following line for testing/debugging
    # print("Running 10 times...")
    # Set counter to 5
    counter = 10
    # Set sleep_speed to 0.05
    sleep_speed = 0.05
    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("Running number:", counter)
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Decrease counter
        counter -= 1
    increase_speed()


if __name__ == '__main__':
    main()
