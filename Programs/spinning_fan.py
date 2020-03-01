#!/usr/bin/env python3
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


def spinning_fan():
    """
    Turns on one arm at a time.
    """
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.5

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
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
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("The speed is now: %s", sleep_speed)
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
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01

    # Start counter at 1, end at 50, increment by 1
    for i in range(1, 51, 1):
        LOGGER.debug("counter = %s", i)
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


def go_really_fast():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    LOGGER.debug("Going really fast...")

    sleep_speed = 0

    # Start counter at 1, end at 100, increment by 1
    for i in range(1, 101, 1):
        LOGGER.debug("counter = %s", i)
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


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    spinning_fan()
    go_fast()
    go_faster()
    go_really_fast()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/spinning_fan.log'
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
