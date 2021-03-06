#!/usr/bin/env python3
"""
Slithering Exploding Snakes

I think the title is self explanatory.

....................

Functions:
- slithering_exploding_snake_12: Lights up the LEDs on arms 1 and 2
- slithering_exploding_snake_13: Lights up the LEDs on arms 1 and 3
- slithering_exploding_snake_21: Lights up the LEDs on arms 2 and 1
- slithering_exploding_snake_23: Lights up the LEDs on arms 2 and 3
- slithering_exploding_snake_31: Lights up the LEDs on arms 3 and 1
- slithering_exploding_snake_32: Lights up the LEDs on arms 3 and 2
- pulse_snake_12_or_21: Pulses the LEDs on arms 1 and 2
- pulse_snake_13_or_31: Pulses the LEDs on arms 1 and 3
- pulse_snake_23_or_32: Pulses the LEDs on arms 2 and 3
- explode_snake_12_or_21: Turns off the LEDs on arms 1 and 2
- explode_snake_13_or_31: Turns off the LEDs on arms 1 and 3
- explode_snake_23_or_32: Turns off the LEDs on arms 2 and 3

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

SLEEP_SPEED = 0.10

########################################################################
#                            Lists                                     #
########################################################################

# LEDs for snakes 12 and 21
SNAKE_12_LEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# LEDs for snakes 13 and 31
SNAKE_13_LEDS = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# LEDs for snakes 23 and 32
SNAKE_23_LEDS = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

########################################################################
#                            Functions                                 #
########################################################################


def slithering_exploding_snake_12():
    """
    Lights up the LEDs on arms 1 and 2
    """
    LOGGER.debug("Snake 12 is slithering...")

    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_12_or_21()
    # Explode Snake 12
    LOGGER.debug("Snake 12 is exploding...")
    explode_snake_12_or_21()
    # Pause before next snake
    sleep(1)


def slithering_exploding_snake_13():
    """
    Lights up the LEDs on arms 1 and 3
    """
    LOGGER.debug("Snake 13 is slithering...")

    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_13_or_31()
    # Explode Snake 13
    LOGGER.debug("Snake 13 is exploding...")
    explode_snake_13_or_31()
    # Pause before next snake
    sleep(1)


def slithering_exploding_snake_21():
    """
    Lights up the LEDs on arms 2 and 1
    """
    LOGGER.debug("Snake 21 is slithering...")

    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_12_or_21()
    # Explode Snake 21
    LOGGER.debug("Snake 21 is exploding...")
    explode_snake_12_or_21()
    # Pause before next snake
    sleep(1)


def slithering_exploding_snake_23():
    """
    Lights up the LEDs on arms 2 and 3
    """
    LOGGER.debug("Snake 23 is slithering...")

    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_23_or_32()
    # Explode Snake 23
    LOGGER.debug("Snake 23 is exploding...")
    explode_snake_23_or_32()
    # Pause before next snake
    sleep(1)


def slithering_exploding_snake_31():
    """
    Lights up the LEDs on arms 3 and 1
    """
    LOGGER.debug("Snake 31 is slithering...")

    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(18, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(5, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(4, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(3, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(2, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(1, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_13_or_31()
    # Explode Snake 31
    LOGGER.debug("Snake 31 is exploding...")
    explode_snake_13_or_31()
    # Pause before next snake
    sleep(1)


def slithering_exploding_snake_32():
    """
    Lights up the LEDs on arms 3 and 2
    """
    LOGGER.debug("Snake 32 is slithering...")

    PYGLOW.led(13, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(14, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(15, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(16, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(17, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(6, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(12, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(11, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(10, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(9, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(8, 100)
    sleep(SLEEP_SPEED)
    PYGLOW.led(7, 100)
    sleep(SLEEP_SPEED)
    # Pulse
    pulse_snake_23_or_32()
    # Explode Snake 32
    LOGGER.debug("Snake 32 is exploding...")
    explode_snake_23_or_32()
    # Pause before next snake
    sleep(1)


def pulse_snake_12_or_21():
    """
    Pulses the LEDs on arms 1 and 2
    """
    LOGGER.debug("Snake is pulsing...")

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(SNAKE_12_LEDS, 100, speed=i, pulse=True)
        sleep(0)
    PYGLOW.led(SNAKE_12_LEDS, 100)
    sleep(1)


def pulse_snake_13_or_31():
    """
    Pulses the LEDs on arms 1 and 3
    """
    LOGGER.debug("Snake is pulsing...")

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(SNAKE_13_LEDS, 100, speed=i, pulse=True)
        sleep(0)
    PYGLOW.led(SNAKE_13_LEDS, 100)
    sleep(1)


def pulse_snake_23_or_32():
    """
    Pulses the LEDs on arms 2 and 3
    """
    LOGGER.debug("Snake is pulsing...")

    # Start pulse speed at 175, end at 225, increment by 1
    for i in range(175, 226, 1):
        LOGGER.debug("Pulse speed is: %s", i)
        PYGLOW.led(SNAKE_23_LEDS, 100, speed=i, pulse=True)
        sleep(0)
    PYGLOW.led(SNAKE_23_LEDS, 100)
    sleep(1)


def explode_snake_12_or_21():
    """
    Turns off the LEDs on arms 1 and 2
    """

    explode_speed = 0.020

    # Explode snake 12 or 21
    PYGLOW.led(18, 0)
    sleep(explode_speed)
    PYGLOW.led(6, 0)
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


def explode_snake_13_or_31():
    """
    Turns off the LEDs on arms 1 and 3
    """

    explode_speed = 0.020

    # Explode snake 13 or 31
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


def explode_snake_23_or_32():
    """
    Turns off the LEDs on arms 2 and 3
    """

    explode_speed = 0.020

    # Explode snake 23 or 32
    PYGLOW.led(12, 0)
    sleep(explode_speed)
    PYGLOW.led(6, 0)
    sleep(explode_speed)
    PYGLOW.led(17, 0)
    sleep(explode_speed)
    PYGLOW.led(11, 0)
    sleep(explode_speed)
    PYGLOW.led(16, 0)
    sleep(explode_speed)
    PYGLOW.led(10, 0)
    sleep(explode_speed)
    PYGLOW.led(15, 0)
    sleep(explode_speed)
    PYGLOW.led(9, 0)
    sleep(explode_speed)
    PYGLOW.led(14, 0)
    sleep(explode_speed)
    PYGLOW.led(8, 0)
    sleep(explode_speed)
    PYGLOW.led(13, 0)
    sleep(explode_speed)
    PYGLOW.led(7, 0)
    sleep(explode_speed)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    # Snakes 12, 13, 21, 23, 31, 32
    slithering_exploding_snake_12()
    slithering_exploding_snake_13()
    slithering_exploding_snake_21()
    slithering_exploding_snake_23()
    slithering_exploding_snake_31()
    slithering_exploding_snake_32()
    # Snakes 12, 23, 31, 13, 32, 21
    slithering_exploding_snake_12()
    slithering_exploding_snake_23()
    slithering_exploding_snake_31()
    slithering_exploding_snake_13()
    slithering_exploding_snake_32()
    slithering_exploding_snake_21()
    # Snakes 13, 12, 23, 21, 31, 32
    slithering_exploding_snake_13()
    slithering_exploding_snake_12()
    slithering_exploding_snake_23()
    slithering_exploding_snake_21()
    slithering_exploding_snake_31()
    slithering_exploding_snake_32()
    # Snakes 13, 32, 21, 12, 23, 31
    slithering_exploding_snake_13()
    slithering_exploding_snake_32()
    slithering_exploding_snake_21()
    slithering_exploding_snake_12()
    slithering_exploding_snake_23()
    slithering_exploding_snake_31()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/slithering_exploding_snakes.log'
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
