#!/usr/bin/env python3
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

Requirements:
    PyGlow.py (many thanks to benleb for this program)
    bfp_piglow_modules.py

You will have these files if you downloaded the entire repository.

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
    LOGGER.debug("Lighting fuse...")
    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def go_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 10 times
    """
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("counter = %s", i)
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    light_the_fuse()
    go_fast()
    go_faster()

    LOGGER.debug("START")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/light_the_fuse.log'
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
