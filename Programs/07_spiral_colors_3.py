#!/usr/bin/env python3
"""
Spiral Colors 3

This is a variation of Spiral Colors. This program lights up the
indivdual colors like in Spiral Colors 2, but the lights are turned off
in the same order they were turned on instead of in reverse order.
Then the speeed gradually increases.

....................

Functions:
- sprial_colors_3_1: Lights up 1 color at a time
- sprial_colors_3_2: Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
- sprial_colors_3_3: Sleep_speed  is 0.01. Cycle through the LEDS 20 times
- sprial_colors_3_4: Sleep_speed is 0. Cycle through the LEDS 100 times
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

Requirements: PyGlow.py

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

from time import sleep
from PyGlow import PyGlow
from bfp_piglow_modules import print_header
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


def spiral_colors_3_1():
    """
    Lights up 1 color at a time
    """

    sleep_speed = 0.25

    while sleep_speed > 0.05:
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


def spiral_colors_3_2():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """

    sleep_speed = 0.05

    while sleep_speed > 0.01:
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


def spiral_colors_3_3():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """

    sleep_speed = 0.01

    # Start counter at 1, end at 20
    for _ in range(1, 20):
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


def spiral_colors_3_4():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """

    sleep_speed = 0

    # Start counter at 1, end at 100
    for _ in range(1, 100):
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


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03: Run Spiral Colors
        spiral_colors_3_1()
        spiral_colors_3_2()
        spiral_colors_3_3()
        spiral_colors_3_4()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
