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

Requirements:
    PyGlow.py
    print_pyglow_header.py
   (You will have these files if you downloaded the entire repository)

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
        increase_speed()
        run_10_times()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def increase_speed():
    """
    Gradually increases the speed at which the LEDs light up
    """
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The current speed is: %s", sleep_speed)
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

    LOGGER.debug("The current sleep speed is: %s", sleep_speed)

    # Start led number at 1, end at 18, increment by 1
    for i in range(1, 19, 1):
        PYGLOW.led(i, led_brightness)
        sleep(sleep_speed)
    sleep(sleep_speed)


def turn_off_leds(sleep_speed):
    """
    Turns off the LEDs one at a time

    Arguments:
        sleep_speed
    """
    LOGGER.debug("Turning off LEDs...")

    LOGGER.debug("The current sleep speed is: %s", sleep_speed)

    # Start led number at 1, end at 18, increment by 1
    for i in range(1, 19, 1):
        PYGLOW.led(i, 0)
        sleep(sleep_speed)
    sleep(sleep_speed)


def run_10_times():
    """ Run 10 times

    Once the program was reached the max set speed, it will cycle
    throught the LEDs 10 times.

    """
    LOGGER.debug("Running 10 times...")

    sleep_speed = 0.05

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("Running number: %s", i)
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)


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
