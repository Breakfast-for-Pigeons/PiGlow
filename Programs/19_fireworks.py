#!/usr/bin/env python3
"""
Fireworks

This program lights up the LEDs from the inside out, and then fades
them - making it look like exploding fireworks.

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


def fireworks():
    """
    This program lights up the LEDs from the inside out, and then fades
    them - making it look like exploding fireworks.
    """

    sleep_speed = 0.025

    # Turn on white
    PYGLOW.color("white", 60)
    sleep(sleep_speed)
    # Turn on blue
    PYGLOW.color("blue", 60)
    sleep(sleep_speed)
    # Fade white
    PYGLOW.color("white", 50)
    sleep(sleep_speed)
    # Turn on green
    PYGLOW.color("green", 60)
    sleep(sleep_speed)
    # Fade white and blue
    PYGLOW.color("white", 40)
    sleep(sleep_speed)
    PYGLOW.color("blue", 50)
    sleep(sleep_speed)
    # Turn on yellow
    PYGLOW.color("yellow", 60)
    sleep(sleep_speed)
    # Fade white, blue, and green
    PYGLOW.color("white", 30)
    sleep(sleep_speed)
    PYGLOW.color("blue", 40)
    sleep(sleep_speed)
    PYGLOW.color("green", 50)
    sleep(sleep_speed)
    # Turn on orange
    PYGLOW.color("orange", 60)
    sleep(sleep_speed)
    # Fade white, blue, green, and yellow
    PYGLOW.color("white", 20)
    sleep(sleep_speed)
    PYGLOW.color("blue", 30)
    sleep(sleep_speed)
    PYGLOW.color("green", 40)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 50)
    sleep(sleep_speed)
    # Turn on red
    PYGLOW.color("red", 60)
    sleep(sleep_speed)
    # Fade white, blue, green, yellow, and orange
    PYGLOW.color("white", 10)
    sleep(sleep_speed)
    PYGLOW.color("blue", 20)
    sleep(sleep_speed)
    PYGLOW.color("green", 30)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 40)
    sleep(sleep_speed)
    PYGLOW.color("orange", 50)
    sleep(sleep_speed)
    # Fade all
    PYGLOW.color("white", 0)
    sleep(sleep_speed)
    PYGLOW.color("blue", 10)
    sleep(sleep_speed)
    PYGLOW.color("green", 20)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 30)
    sleep(sleep_speed)
    PYGLOW.color("orange", 40)
    sleep(sleep_speed)
    PYGLOW.color("red", 50)
    sleep(sleep_speed)
    # Fade blue, green, yellow, orange, and red
    PYGLOW.color("blue", 0)
    sleep(sleep_speed)
    PYGLOW.color("green", 10)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 20)
    sleep(sleep_speed)
    PYGLOW.color("orange", 30)
    sleep(sleep_speed)
    PYGLOW.color("red", 40)
    sleep(sleep_speed)
    # Fade green, yellow, orange, and red
    PYGLOW.color("green", 0)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 10)
    sleep(sleep_speed)
    PYGLOW.color("orange", 20)
    sleep(sleep_speed)
    PYGLOW.color("red", 30)
    sleep(sleep_speed)
    # Fade yellow, orange, and red
    PYGLOW.color("yellow", 0)
    sleep(sleep_speed)
    PYGLOW.color("orange", 10)
    sleep(sleep_speed)
    PYGLOW.color("red", 20)
    sleep(sleep_speed)
    # Fade orange, and red
    PYGLOW.color("orange", 0)
    sleep(sleep_speed)
    PYGLOW.color("red", 10)
    sleep(sleep_speed)
    # Fade red
    PYGLOW.color("red", 0)
    sleep(sleep_speed)
    # Pause 1 second before the next one
    sleep(1)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("Fireworks #%s", i)
        fireworks()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/19_firworks.log'
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
