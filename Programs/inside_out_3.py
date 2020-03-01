#!/usr/bin/env python3
"""
Inside Out 3

A variation of Inside Out. This program lights up the
indivdual colors like in Inward Out 2, but the lights are
turned off in the same order they were turned on instead
of in reverse order.Then the speeed gradually increases.

....................

Functions:
- inside_out_3a: Lights up 1 color at a time
- inside_out_3b: Sleep_speed goes from 0.05 to 0.01 in decrements
                 of 0.0025
- inside_out_3c: Sleep_speed  is 0.01. Cycle through the LEDS 20 times
- inside_out_3d: Sleep_speed is 0. Cycle through the LEDS 100 times
- red_leds_on: Lights up the red LEDs one at a time
- red_leds_off: Turns off the red LEDs one at a time
- orange_leds_on: Lights up the orange LEDs one at a time
- orange_leds_off: Turns off the orange LEDs one at a time
- yellow_leds_on: Lights up the yellow LEDs one at a time
- yellow_leds_off: Turns off the yellow LEDs one at a time
- green_leds_on: Lights up the green LEDs one at a time
- green_leds_off: Turns off the green LEDs one at a time
- blue_leds_on: Lights up the blue LEDs one at a time
- blue_leds_off: Turns off the blue LEDs one at a time
- white_leds_on: : Lights up the  white LEDs one at a time
- white_leds_off: Turns off the white LEDs one at a time

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

# Feel free to modify the brightness setting below
LED_BRIGHTNESS = 100

########################################################################
#                            Functions                                 #
########################################################################


def red_leds_on(sleep_speed):
    """
    Lights up the red LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Red
    PYGLOW.led(13, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(1, LED_BRIGHTNESS)
    sleep(sleep_speed)


def red_leds_off(sleep_speed):
    """
    Turns off the red LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Red
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(1, 0)
    sleep(sleep_speed)


def orange_leds_on(sleep_speed):
    """
    Lights up the orange LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Orange
    PYGLOW.led(14, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(2, LED_BRIGHTNESS)
    sleep(sleep_speed)


def orange_leds_off(sleep_speed):
    """
    Turns off the orange LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Orange
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(2, 0)
    sleep(sleep_speed)


def yellow_leds_on(sleep_speed):
    """
    Lights up the yellow LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Yellow
    PYGLOW.led(15, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(3, LED_BRIGHTNESS)
    sleep(sleep_speed)


def yellow_leds_off(sleep_speed):
    """
    Turns off the yellow LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Yellow
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(3, 0)
    sleep(sleep_speed)


def green_leds_on(sleep_speed):
    """
    Lights up the green LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Green
    PYGLOW.led(16, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(4, LED_BRIGHTNESS)
    sleep(sleep_speed)


def green_leds_off(sleep_speed):
    """
    Turns off the green LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Green
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(4, 0)
    sleep(sleep_speed)


def blue_leds_on(sleep_speed):
    """
    Lights up the blue LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Blue
    PYGLOW.led(17, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(5, LED_BRIGHTNESS)
    sleep(sleep_speed)


def blue_leds_off(sleep_speed):
    """
    Turns off the blue LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, Blue
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(5, 0)
    sleep(sleep_speed)


def white_leds_on(sleep_speed):
    """
    Lights up the white LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, White
    PYGLOW.led(18, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(6, LED_BRIGHTNESS)
    sleep(sleep_speed)


def white_leds_off(sleep_speed):
    """
    Turns off the white LEDs one at a time
    """

    sleep_speed = sleep_speed

    # Arm 1, White
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(6, 0)
    sleep(sleep_speed)


def inside_out_3a():
    """
    Lights up 1 color at a time

    Speed goes from 0.25 to 0.05 in decrements of 0.05
    """
    LOGGER.debug("Function: inside_out_3a")
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def inside_out_3b():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Function: inside_out_3b")
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025


def inside_out_3c():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    LOGGER.debug("Function: inside_out_3c")
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01

    # Start counter at 1, end at 20, increment by 1
    for i in range(1, 21, 1):
        LOGGER.debug("counter = %s", i)
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)


def inside_out_3d():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    LOGGER.debug("Function: inside_out_3d")
    LOGGER.debug("Going really fast...")

    sleep_speed = 0

    # Start counter at 1, end at 100, increment by 1
    for i in range(1, 101, 1):
        LOGGER.debug("counter = %s", i)
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    inside_out_3a()
    inside_out_3b()
    inside_out_3c()
    inside_out_3d()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exits.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/inside_out_3.log'
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
