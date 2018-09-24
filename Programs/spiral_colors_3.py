#!/usr/bin/python3
"""
Spiral Colors 3

This is a variation of Spiral Colors. This program lights up the
indivdual colors like in Spiral Colors 2, but the lights are turned off
in the same order they were turned on instead of in reverse order.
Then the speeed gradually increases.

....................

Functions:
- sprial_colors: Lights up 1 color at a time
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
- go_fast: Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
- go_faster: Sleep_speed  is 0.01. Cycle through the LEDS 20 times
- go_really_fast: Sleep_speed is 0. Cycle through the LEDS 100 times
- delete_empty_logs: Deletes empty log fles
- stop: Print exit message and turn off the PiGlow

....................

Requirements:
    PyGlow.py (many thanks to benleb for this program)
    print_piglow_header.py

You will have these files if you downloaded the entire repository.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import os
import logging
from time import sleep
from PyGlow import PyGlow
from print_piglow_header import print_piglow_header

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

# Logging
LOG = 'spiral_colors_3.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)    # Nothing will log unless changed to DEBUG
FORMATTER = logging.Formatter(fmt=LOG_FORMAT,
                              datefmt='%m/%d/%y %I:%M:%S %p:')
FILE_HANDLER = logging.FileHandler(LOG, 'w')
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    print_piglow_header()

    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")
    try:
        spiral_colors()
        go_fast()
        go_faster()
        go_really_fast()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def red_leds_on(sleep_speed):
    """
    Lights up the red LEDs one at a time

    Arguments:
        sleep_speed: the time to wait between LEDs
    """
    LOGGER.debug("Lighting up red LEDs...")

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, Red
    PYGLOW.led(1, led_brightness)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, led_brightness)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, led_brightness)
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

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, Orange
    PYGLOW.led(2, led_brightness)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, led_brightness)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, led_brightness)
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

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, Yellow
    PYGLOW.led(3, led_brightness)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, led_brightness)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, led_brightness)
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

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, Green
    PYGLOW.led(4, led_brightness)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, led_brightness)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, led_brightness)
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

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, Blue
    PYGLOW.led(5, led_brightness)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, led_brightness)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, led_brightness)
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

    # Feel free to modify the brightness setting below
    led_brightness = 100
    sleep_speed = sleep_speed

    # Arm 1, White
    PYGLOW.led(6, led_brightness)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, led_brightness)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, led_brightness)
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


def spiral_colors():
    """
    Lights up 1 color at a time
    """
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
        red_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        white_leds_off(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def go_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("sleep speed is = %s", sleep_speed)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        red_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        white_leds_off(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01
    counter = 20

    while counter > 0:
        LOGGER.debug("counter = %s", counter)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        red_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        white_leds_off(sleep_speed)
        # decrease counter
        counter -= 1


def go_really_fast():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    LOGGER.debug("Going really fast...")

    sleep_speed = 0
    counter = 100

    while counter > 0:
        LOGGER.debug("counter = %s", counter)
        # Turn on LEDs
        red_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        white_leds_on(sleep_speed)
        # Turn off LEDs
        red_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        white_leds_off(sleep_speed)
        # decrease counter
        counter -= 1


def delete_empty_logs():
    """
    Delete empty log fles

    Log files will always be created. But they will be empty if the
    log level is set to anything higher than DEBUG, since only DEBUG
    messages are logged. If the log files are empty, they will be
    deleted.
    """

    logs = [LOG, 'print_piglow_header.log']

    for log in logs:
        if os.stat(log).st_size == 0:
            os.remove(log)


def stop():
    """
    Print exit message and turn off the PiGlow
    """
    LOGGER.debug("END")
    delete_empty_logs()
    print("\nExiting program.")
    PYGLOW.all(0)


if __name__ == '__main__':
    main()
