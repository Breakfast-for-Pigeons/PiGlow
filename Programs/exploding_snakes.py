#!/usr/bin/env python3
"""
Exploding Snakes

I think the title is self explanatory. The snakes start pulsing and
eventually explode.

....................

Functions:

- explode_snake_12_or_21: Lights up and turns off the LEDs on arms 1 and 2
- explode_snake_13_or_31: Lights up and turns off the LEDs on arms 1 and 3
- explode_snake_23_or_32: Lights up and turns off the LEDs on arms 2 and 3

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


def exploding_snake_12():
    """
    Lights up and turns off the LEDs on arms 1 and 2
    """

    # LEDs for snakes 12 and 21
    snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]

    explode_speed = 0.020

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(snake_12_leds, 100, speed=i, pulse=True)
        sleep(0)

    # Pause 1 second before exploding
    PYGLOW.led(snake_12_leds, 100)
    sleep(1)

    # Explode Snake 12
    LOGGER.debug("Exploding Snake 12...")
    PYGLOW.led(6, 0)
    sleep(explode_speed)
    PYGLOW.led(18, 0)
    sleep(explode_speed)
    PYGLOW.led(11, 0)
    sleep(explode_speed)
    PYGLOW.led(5, 0)
    sleep(explode_speed)
    PYGLOW.led(10, 0)
    sleep(explode_speed)
    PYGLOW.led(4, 0)
    sleep(explode_speed)
    PYGLOW.led(9, 0)
    sleep(explode_speed)
    PYGLOW.led(3, 0)
    sleep(explode_speed)
    PYGLOW.led(8, 0)
    sleep(explode_speed)
    PYGLOW.led(2, 0)
    sleep(explode_speed)
    PYGLOW.led(7, 0)
    sleep(explode_speed)
    PYGLOW.led(1, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


def exploding_snake_13():
    """
    Lights up and turns off the LEDs on arms 1 and 3
    """

    # LEDs for snakes 13 and 31
    snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]

    explode_speed = 0.020

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(snake_13_leds, 100, speed=i, pulse=True)
        sleep(0)

    # Pause 1 second before exploding
    PYGLOW.led(snake_13_leds, 100)
    sleep(1)

    # Explode Snake 13
    LOGGER.debug("Exploding Snake 13...")
    PYGLOW.led(18, 0)
    sleep(explode_speed)
    PYGLOW.led(12, 0)
    sleep(explode_speed)
    PYGLOW.led(17, 0)
    sleep(explode_speed)
    PYGLOW.led(5, 0)
    sleep(explode_speed)
    PYGLOW.led(16, 0)
    sleep(explode_speed)
    PYGLOW.led(4, 0)
    sleep(explode_speed)
    PYGLOW.led(15, 0)
    sleep(explode_speed)
    PYGLOW.led(3, 0)
    sleep(explode_speed)
    PYGLOW.led(14, 0)
    sleep(explode_speed)
    PYGLOW.led(2, 0)
    sleep(explode_speed)
    PYGLOW.led(13, 0)
    sleep(explode_speed)
    PYGLOW.led(1, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


def exploding_snake_23():
    """
    Lights up and turns off the LEDs on arms 2 and 3
    """

    # LEDs for snakes 23 and 32
    snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    explode_speed = 0.020

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(snake_23_leds, 100, speed=i, pulse=True)
        sleep(0)

    # Pause 1 second before exploding
    PYGLOW.led(snake_23_leds, 100)
    sleep(1)

    # Explode Snake 13
    LOGGER.debug("Exploding Snake 23...")
    PYGLOW.led(6, 0)
    sleep(explode_speed)
    PYGLOW.led(12, 0)
    sleep(explode_speed)
    PYGLOW.led(11, 0)
    sleep(explode_speed)
    PYGLOW.led(17, 0)
    sleep(explode_speed)
    PYGLOW.led(10, 0)
    sleep(explode_speed)
    PYGLOW.led(16, 0)
    sleep(explode_speed)
    PYGLOW.led(9, 0)
    sleep(explode_speed)
    PYGLOW.led(15, 0)
    sleep(explode_speed)
    PYGLOW.led(8, 0)
    sleep(explode_speed)
    PYGLOW.led(14, 0)
    sleep(explode_speed)
    PYGLOW.led(7, 0)
    sleep(explode_speed)
    PYGLOW.led(13, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    # 12, 13, 23
    exploding_snake_12()
    exploding_snake_13()
    exploding_snake_23()
    # 13, 23, 12
    exploding_snake_13()
    exploding_snake_23()
    exploding_snake_12()
    # 23, 12, 13
    exploding_snake_23()
    exploding_snake_12()
    exploding_snake_13()
    # 12, 23, 13
    exploding_snake_12()
    exploding_snake_23()
    exploding_snake_13()
    # 23, 13, 12
    exploding_snake_23()
    exploding_snake_13()
    exploding_snake_12()
    # 13, 12, 23
    exploding_snake_13()
    exploding_snake_12()
    exploding_snake_23()

    LOGGER.debug("START")

    delete_empty_logs(LOG)
    stop()



if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/exploding_snakes.log'
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
