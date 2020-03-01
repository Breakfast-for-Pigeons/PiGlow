#!/usr/bin/env python3
"""
Confluence

This program is basically my "Light the Fuse" program in
reverse. It lights up 2 arms at once and converges into the
third arm.

....................

Functions:

- confluence_slow: Controls which fuse to light
- confluence_fast: Lights up arm 1, then 2 and 3
- confluence_1_and_2_into_3: Lights up arms 1 and 2, then arm 3
- confluence_1_and_3_into_2: Lights up arms 1 and 3, then arm 2
- confluence_2_and_3_into_1: Lights up arms 2 and 3, then arm 1
- delete_empty_logs: Deletes empty log fles
- stop: Print exit message and turn off the PiGlow

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


def confluence_2_and_3_into_1(sleep_speed):
    """
    Lights up arms 2 and 3, then arm 1
    """
    LOGGER.debug("Confluence 2 and 3 into 1...")
    # Arm 2 and 3, Red
    PYGLOW.led(7, 120)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 120)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 120)
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
    sleep(1)
    # Turn 'em off
    PYGLOW.all(0)
    sleep(1)


def confluence_1_and_3_into_2(sleep_speed):
    """
    Lights up arms 1 and 3, then arm 2
    """
    LOGGER.debug("Confluence 1 and 3 into 2...")
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
    sleep(1)
    # Turn 'em off
    PYGLOW.all(0)
    sleep(1)


def confluence_1_and_2_into_3(sleep_speed):
    """
    Lights up arms 1 and 3, then arm 2
    """
    LOGGER.debug("Confluence 1 and 2 into 3...")
    # Arm 1 and 2, Red
    PYGLOW.led(1, 120)
    PYGLOW.led(7, 120)
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
    sleep(1)
    # Turn 'em off
    PYGLOW.all(0)
    sleep(1)


def confluence_slow():
    """
    Gradually increases the speed at which the LEDs light up
    """
    LOGGER.debug("Confluence slow")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def confluence_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Confluence slow")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("sleep_speed = %s", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    confluence_slow()
    confluence_fast()

    LOGGER.debug("START")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/38_confluence.log'
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
