#!/usr/bin/env python3
"""
Reverse Spiral Colors 2

This program lights up the indivdual colors like in
Spiral Colors 2, but counter clockwise.

....................

Functions:
- reverse_sprial_colors_2a: Lights up 1 color at a time
- reverse_sprial_colors_2b: Sleep_speed goes from 0.05 to 0.01 in
                            decrements of 0.0025
- reverse_sprial_colors_2c: Sleep_speed  is 0.01. Cycle through the LEDS
                            20 times
- reverse_sprial_colors_2d: Sleep_speed is 0. Cycle through the LEDS 100
                            times
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

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up red LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Red
    PYGLOW.led(1, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, LED_BRIGHTNESS)
    sleep(sleep_speed)


def red_leds_off(sleep_speed):
    """
    Turns off the red LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off red LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Red
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, 0)
    sleep(sleep_speed)


def orange_leds_on(sleep_speed):
    """
    Lights up the orange LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up orange LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Orange
    PYGLOW.led(2, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, LED_BRIGHTNESS)
    sleep(sleep_speed)


def orange_leds_off(sleep_speed):
    """
    Turns off the orange LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off orange LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Orange
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 0)
    sleep(sleep_speed)


def yellow_leds_on(sleep_speed):
    """
    Lights up the yellow LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up yellow LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Yellow
    PYGLOW.led(3, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, LED_BRIGHTNESS)
    sleep(sleep_speed)


def yellow_leds_off(sleep_speed):
    """
    Turns off the yellow LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off yellow LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Yellow
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 0)
    sleep(sleep_speed)


def green_leds_on(sleep_speed):
    """
    Lights up the green LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up green LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Green
    PYGLOW.led(4, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, LED_BRIGHTNESS)
    sleep(sleep_speed)


def green_leds_off(sleep_speed):
    """
    Turns off the green LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off green LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Green
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, 0)
    sleep(sleep_speed)


def blue_leds_on(sleep_speed):
    """
    Lights up the blue LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up blue LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Blue
    PYGLOW.led(5, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, LED_BRIGHTNESS)
    sleep(sleep_speed)


def blue_leds_off(sleep_speed):
    """
    Turns off the blue LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off blue LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, Blue
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 0)
    sleep(sleep_speed)


def white_leds_on(sleep_speed):
    """
    Lights up the white LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up white LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, White
    PYGLOW.led(6, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, LED_BRIGHTNESS)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, LED_BRIGHTNESS)
    sleep(sleep_speed)


def white_leds_off(sleep_speed):
    """
    Turns off the white LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Turning off white LEDs...")

    sleep_speed = sleep_speed

    # Arm 1, White
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, 0)
    sleep(sleep_speed)


def reverse_sprial_colors_2a():
    """
    Lights up 1 color at a time
    """
    LOGGER.debug("Function: reverse_spiral_colors_2a")
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def reverse_sprial_colors_2b():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Function: reverse_spiral_colors_2b")
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("sleep speed = %s", sleep_speed)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025


def reverse_sprial_colors_2c():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    LOGGER.debug("Function: reverse_spiral_colors_2c")
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01

    # Start counter at 1, end at 20, increment by 1
    for i in range(1, 21, 1):
        LOGGER.debug("counter = %s", i)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)


def reverse_sprial_colors_2d():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    LOGGER.debug("Function: reverse_spiral_colors_2d")
    LOGGER.debug("Going really fast...")

    sleep_speed = 0

    # Start counter at 1, end at 100, increment by 1
    for i in range(1, 101, 1):
        LOGGER.debug("counter = %s", i)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
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
    reverse_sprial_colors_2a()
    reverse_sprial_colors_2b()
    reverse_sprial_colors_2c()
    reverse_sprial_colors_2d()
    LOGGER.debug("END")
    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exits.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/reverse_spiral_colors_2.log'
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
