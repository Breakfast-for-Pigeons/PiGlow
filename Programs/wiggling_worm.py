#!/usr/bin/env python3
"""
Wiggling Worm

I think the title is self explanatory. I originally had an idea called
"Spinning Snakes" where I took the snake program and sped it up. This
was the unexpected result.

....................

Functions:
- snake_12: Lights up the LEDs on arms 1 and 2
- snake_13: Lights up the LEDs on arms 1 and 3
- snake_23: Lights up the LEDs on arms 2 and 3

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


def snake_12():
    """
    Lights up the LEDs on arms 1 and 2
    """

    # Snake 12 LEDs (Same lights as Snake 21 - Since they are not
    # slithering, the order doesn't matter)
    snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]

    PYGLOW.set_leds(snake_12_leds, 100)
    PYGLOW.update_leds()
    sleep(1)
    PYGLOW.set_leds(snake_12_leds, 0)
    PYGLOW.update_leds()


def snake_13():
    """
    Lights up the LEDs on arms 1 and 3
    """

    # Snake 13 LEDs (Same lights as Snake 31 - Since they are not
    # slithering, the order doesn't matter)
    snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]

    PYGLOW.set_leds(snake_13_leds, 100)
    PYGLOW.update_leds()
    sleep(1)
    PYGLOW.set_leds(snake_13_leds, 0)
    PYGLOW.update_leds()


def snake_23():
    """
    Lights up the LEDs on arms 2 and 3
    """

    # Snake 23 LEDs (Same lights as Snake 32 - Since they are not
    # slithering, the order doesn't matter)
    snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    PYGLOW.set_leds(snake_23_leds, 100)
    PYGLOW.update_leds()
    sleep(1)
    PYGLOW.set_leds(snake_23_leds, 0)
    PYGLOW.update_leds()


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    # Start counter at 1, end at 3, increment by 1
    for i in range(1, 4, 1):
        LOGGER.debug("counter = %s", i)
        snake_12()
        snake_23()
        snake_13()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/wiggling_worm.log'
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
