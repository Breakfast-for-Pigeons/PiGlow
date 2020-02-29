#!/usr/bin/env python3
"""
Pulsing Snakes

I think the title is self explanatory.

....................

Functions:
- pulsing_snake_12: Lights up and pulses the LEDs on arms 1 and 2
- pulsing_snake_13: Lights up and pulses the LEDs on arms 1 and 3
- pulsing_snake_23: Lights up and pulses the LEDs on arms 2 and 3

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


def pulsing_snake_12():
    """
    Lights up and pulses the LEDs on arms 1 and 2
    """
    LOGGER.debug("Pulsing Snake 12")

    # Snake 12 LEDs (Same lights as Snake 21 - Since they are not
    # slithering, the order doesn't matter)
    snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]

    # Start pulse speed at 200, end at 150, decrement by 1
    for i in range(200, 149, -1):
        PYGLOW.set_leds(snake_12_leds, 100, speed=i,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
    PYGLOW.set_leds(snake_12_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


def pulsing_snake_13():
    """
    Lights up and pulses the LEDs on arms 1 and 3
    """
    LOGGER.debug("Pulsing Snake 13")

    # Snake 13 LEDs (Same lights as Snake 31 - Since they are not
    # slithering, the order doesn't matter)
    snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]

    # Start pulse speed at 200, end at 150, decrement by 1
    for i in range(200, 149, -1):
        PYGLOW.set_leds(snake_13_leds, 100, speed=i,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
    PYGLOW.set_leds(snake_13_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


def pulsing_snake_23():
    """
    Lights up and pulses the LEDs on arms 2 and 3
    """
    LOGGER.debug("Pulsing Snake 23")

    # Snake 23 LEDs (Same lights as Snake 32 - Since they are not
    # slithering, the order doesn't matter)
    snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    # Start pulse speed at 200, end at 150, decrement by 1
    for i in range(200, 149, -1):
        PYGLOW.set_leds(snake_23_leds, 100, speed=i,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
    PYGLOW.set_leds(snake_23_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    # 12, 13, 23
    pulsing_snake_12()
    pulsing_snake_13()
    pulsing_snake_23()
    # 13, 23, 12
    pulsing_snake_13()
    pulsing_snake_23()
    pulsing_snake_12()
    # 23, 12, 13
    pulsing_snake_23()
    pulsing_snake_12()
    pulsing_snake_13()
    # 12, 23, 13
    pulsing_snake_12()
    pulsing_snake_23()
    pulsing_snake_13()
    # 23, 13, 12
    pulsing_snake_23()
    pulsing_snake_13()
    pulsing_snake_12()
    # 13, 12, 23
    pulsing_snake_13()
    pulsing_snake_12()
    pulsing_snake_23()

    LOGGER.debug("START")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/30_pulsing_snakes.log'
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
