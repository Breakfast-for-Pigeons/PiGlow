#!/usr/bin/python3
"""
Spiral Arms

This program lights up the LEDs on arm 1 one at at time,
then arm 2, then arm 3. Then turns off the lights one at a
time. Then increases the speed and goes through the entire
process again.

....................

Functions:
- spiral_arms: Gradually increases the speed
- turn_on_leds: Turns on the LEDs one at a time
- turn_off_leds: Turns off the LEDs one at a time
- run_10_times: Cycles throught the LEDs 10 times
- delete_empty_logs: Deletes empty log fles
- stop: Print exit message and turn off the PiGlow

....................

Requirements: PyGlow.py

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import os
import logging
from time import sleep
from PyGlow import PyGlow
from print_piglow_header import print_piglow_header

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

# Logging
LOG = 'spiral_arms.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)    # Nothing will log unless changed to DEBUG
FORMATTER = logging.Formatter(fmt=LOG_FORMAT,
                              datefmt='%m/%d/%y %I:%M:%S %p:')
FILE_HANDLER = logging.FileHandler(LOG, 'w')
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    print_piglow_header()

    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")
    try:
        spiral_arms()
        run_10_times()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def spiral_arms():
    """
    Gradually increases the speed at which the LEDs light up
    """
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print "The current speed is:", sleep_speed
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def turn_on_leds(sleep_speed):
    """
    Turns on the LEDs one at a time

    Arguments:
        sleep_speed
    """
    LOGGER.debug("Turning on LEDs...")

    # Feel free to modify the brightness setting below
    led_brightness = 100

    # But don't change the led_number
    led_number = 1

    LOGGER.debug("The current sleep speed (turn on LEDs) is: %s", sleep_speed)

    while led_number < 19:
        PYGLOW.led(led_number, led_brightness)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)


def turn_off_leds(sleep_speed):
    """
    Turns off the LEDs one at a time

    Arguments:
        sleep_speed
    """
    LOGGER.debug("Turning off LEDs...")

    # Set (or Reset) LED number
    led_number = 1

    LOGGER.debug("The current sleep speed (turn off LEDs) is: %s", sleep_speed)

    # Turn off LEDs one at a time
    while led_number < 19:
        PYGLOW.led(led_number, 0)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)


def run_10_times():
    """ Run 10 times

    Once the program was reached the max set speed, it will cycle
    throught the LEDs 10 times.

    """
    LOGGER.debug("Running 10 times...")

    counter = 10
    sleep_speed = 0.05

    while counter > 0:
        LOGGER.debug("Running number: %s", counter)
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Decrease counter
        counter -= 1


def delete_empty_logs():
    """
    Delete empty log fles

    Log files will always be created. But they will be empty if the
    log level is set to anything higher than DEBUG, since only DEBUG
    messages are logged. If the log files are empty, they will be
    deleted.
    """

    logs = [LOG, 'print_piglow_header.log']

    for log in logs:
        if os.stat(log).st_size == 0:
            os.remove(log)


def stop():
    """
    Print exit message and turn off the PiGlow
    """
    LOGGER.debug("END")
    delete_empty_logs()
    print("\nExiting program.")
    PYGLOW.all(0)


if __name__ == '__main__':
    main()
