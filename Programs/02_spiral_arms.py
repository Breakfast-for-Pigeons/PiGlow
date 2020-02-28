#!/usr/bin/env python3
"""
Spiral Arms

This program lights up the LEDs on arm 1 one at at time,
then arm 2, then arm 3. Then turns off the lights one at a
time. Then increases the speed and goes through the entire
process again.

....................

Functions:
- spiral_arms_1: Gradually increases the speed
- spiral_arms_2: Cycles through the LEDs 10 times
- turn_on_leds: Turns on the LEDs one at a time
- turn_off_leds: Turns off the LEDs one at a time


....................

Requirements:
    PyGlow.py
    bfp_piglow_modules.py

You will have these files if you downloaded the entire repository

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import logging
from time import sleep
from PyGlow import PyGlow
from bfp_piglow_modules import print_header
from bfp_piglow_modules import check_log_directory
from bfp_piglow_modules import delete_empty_logs
from bfp_piglow_modules import stop

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

########################################################################
#                            Functions                                 #
########################################################################


def spiral_arms_1():
    """
    Turns on the LEDs one at a time until all 18 LEDs are lit
    up at the same time. Then turns off the LEDs one at a time
    until all 18 LEDs are off. This process is done a total of
    5 times, gradually increasing the speed each time.
    """
    LOGGER.debug("Function: spiral arms 1:")
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The current speed is: %s", sleep_speed)
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def spiral_arms_2():
    """
    Turns on the LEDs one at a time until all 18 LEDs are lit
    up at the same time. Then turns off the LEDs one at a time
    until all 18 LEDs are off. This process is done a total of
    10 times at the sleep_speed of 0.05.

    """
    LOGGER.debug("Function: spiral arms 2:")
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.05

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("Running number: %s", i)
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)


def turn_on_leds(sleep_speed):
    """
    Turns on the LEDs one at a time until all 18 LEDs are lit
    up at the same time.

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
    Turns off the LEDs one at a time until all 18 LEDs are off.

    Arguments:
        sleep_speed
    """
    LOGGER.debug("Turning off LEDs...")
    LOGGER.debug("The current sleep speed is: %s", sleep_speed)

    # Start LED number at 1, end at 18, increment by 1
    for i in range(1, 19, 1):
        PYGLOW.led(i, 0)
        sleep(sleep_speed)

    sleep(sleep_speed)


def main():
    """
    This is the main function.
    """
    LOGGER.debug("START")
    spiral_arms_1()
    spiral_arms_2()
    LOGGER.debug("END")
    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exits.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/02_spiral_arms.log'
        LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: \
                      %(levelname)s: %(message)s'
        LOGGER = logging.getLogger(__name__)
        # Nothing will log unless logging level is changed to DEBUG
        LOGGER.setLevel(logging.ERROR)
        FORMATTER = logging.Formatter(fmt=LOG_FORMAT,
                                      datefmt='%m/%d/%y %I:%M:%S %p:')
        FILE_HANDLER = logging.FileHandler(LOG, 'w')
        FILE_HANDLER.setFormatter(FORMATTER)
        LOGGER.addHandler(FILE_HANDLER)
        # STEP03: Print header
        print_header()
        # STEP04: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP05: Run the main function
        main()
    except KeyboardInterrupt:
        delete_empty_logs(LOG)
        stop()
