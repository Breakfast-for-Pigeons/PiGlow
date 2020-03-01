#!/usr/bin/env python3
"""
Rippling Confluence

This program is basically my "Light the Fuse" program in
reverse. It lights up 2 arms at once and converges into the
third arm. It also creates "ripples" by dimming the brightness of
the LEDs one at a time.

....................

Functions:

- confluence_slow: Controls which fuse to light
- confluence_fast: Lights up arm 1, then 2 and 3
- confluence_1_and_2_into_3: Lights up arms 1 and 2, then arm 3
- confluence_1_and_3_into_2: Lights up arms 1 and 3, then arm 2
- confluence_2_and_3_into_1: Lights up arms 2 and 3, then arm 1
- rippling_confluence_1: Ripples the lights on arms 2 and 3, then arm 1
- rippling_confluence_2: Ripples the lights on arms 1 and 3, then arm 2
- rippling_confluence_3: Ripples the lights on arms 1 and 2, then arm 3
- fading_confluence_1: Fades the lights on arms 2 and 3, then arm 1
- fading_confluence_2: Fades the lights on arms 1 and 3, then arm 2
- fading_confluence_3: Fades the lights on arms 1 and 2, then arm 3

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


def confluence_2_and_3_into_1(sleep_speed):
    """
    Lights up arms 2 and 3, then arm 1
    """
    LOGGER.debug("Confluence 2 and 3 into 1...")

    sleep_speed = sleep_speed

    # Arm 2 and 3, Red
    PYGLOW.led(7, 120)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 120)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 120)
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 120)
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 120)
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 120)
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 1, White
    PYGLOW.led(6, 120)
    sleep(sleep_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 120)
    sleep(sleep_speed)
    # Arm 1, Green
    PYGLOW.led(4, 120)
    sleep(sleep_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 120)
    sleep(sleep_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 120)
    sleep(sleep_speed)
    # Arm 1, Red
    PYGLOW.led(1, 120)
    sleep(sleep_speed)
    # Ripple
    for i in range(1, 11, 1):
        LOGGER.debug("Ripple count: %s", i)
        rippling_confluence_1(sleep_speed)
    # Fade
    fading_confluence_1()


def confluence_1_and_3_into_2(sleep_speed):
    """
    Lights up arms 1 and 3, then arm 2
    """
    LOGGER.debug("Confluence 1 and 3 into 2...")

    sleep_speed = sleep_speed

    # Arm 1 and 3, Red
    PYGLOW.led(1, 120)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 120)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 120)
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 120)
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 120)
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 120)
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, 120)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 120)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, 120)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 120)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 120)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, 120)
    sleep(sleep_speed)
    for i in range(1, 11, 1):
        LOGGER.debug("Ripple count: %s", i)
        rippling_confluence_2(sleep_speed)
    fading_confluence_2()
    sleep(1)


def confluence_1_and_2_into_3(sleep_speed):
    """
    Lights up arms 1 and 2, then arm 3
    """
    LOGGER.debug("Confluence 1 and 2 into 3...")

    sleep_speed = sleep_speed

    # Arm 1 and 2, Red
    PYGLOW.led(1, 120)
    PYGLOW.led(7, 120)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 120)
    PYGLOW.led(8, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 120)
    PYGLOW.led(9, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 120)
    PYGLOW.led(10, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 120)
    PYGLOW.led(11, 120)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 120)
    PYGLOW.led(12, 120)
    sleep(sleep_speed)
    # Arm 3, White
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    # Arm 3, Green
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    # Arm 3, Red
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    # Ripple
    for i in range(1, 11, 1):
        LOGGER.debug("Ripple count: %s", i)
        rippling_confluence_3(sleep_speed)
    # Fade
    fading_confluence_3()
    sleep(1)


def rippling_confluence_1(sleep_speed):
    """
    Ripples the lights on arms 2 and 3, then arm 1
    """
    LOGGER.debug("Rippling Confluence 1...")

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    LOGGER.debug("ripple speed is: %s", ripple_speed)

    # Ripple
    # Arm 2 and 3, Red
    PYGLOW.led(7, 60)
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    # Arm 2 and 3, Red
    PYGLOW.led(7, 120)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Orange
    PYGLOW.led(8, 60)
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(8, 120)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Yellow
    PYGLOW.led(9, 60)
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(9, 120)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Green
    PYGLOW.led(10, 60)
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(10, 120)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, Blue
    PYGLOW.led(11, 60)
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(11, 120)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 2 and 3, White
    PYGLOW.led(12, 60)
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(12, 120)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 1, White
    PYGLOW.led(6, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    sleep(ripple_speed)
    # Arm 1, Blue
    PYGLOW.led(5, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    sleep(ripple_speed)
    # Arm 1, Green
    PYGLOW.led(4, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    sleep(ripple_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    sleep(ripple_speed)
    # Arm 1, Orange
    PYGLOW.led(2, 80)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    sleep(ripple_speed)
    # Arm 1, Red
    PYGLOW.led(1, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    sleep(ripple_speed)


def rippling_confluence_2(sleep_speed):
    """
    Ripples the lights on arms 1 and 3, then arm 2
    """
    LOGGER.debug("Rippling Confluence 1...")

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    LOGGER.debug("ripple speed is: %s", ripple_speed)

    # Ripple
    # Arm 1 and 3, Red
    PYGLOW.led(1, 60)
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Orange
    PYGLOW.led(2, 60)
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Yellow
    PYGLOW.led(3, 60)
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Green
    PYGLOW.led(4, 60)
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, Blue
    PYGLOW.led(5, 60)
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 1 and 3, White
    PYGLOW.led(6, 60)
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 2, White
    PYGLOW.led(12, 60)
    sleep(ripple_speed)
    PYGLOW.led(12, 120)
    sleep(ripple_speed)
    # Arm 2, Blue
    PYGLOW.led(11, 60)
    sleep(ripple_speed)
    PYGLOW.led(11, 120)
    sleep(ripple_speed)
    # Arm 2, Green
    PYGLOW.led(10, 60)
    sleep(ripple_speed)
    PYGLOW.led(10, 120)
    sleep(ripple_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, 60)
    sleep(ripple_speed)
    PYGLOW.led(9, 120)
    sleep(ripple_speed)
    # Arm 2, Orange
    PYGLOW.led(8, 60)
    sleep(ripple_speed)
    PYGLOW.led(8, 120)
    sleep(ripple_speed)
    # Arm 2, Red
    PYGLOW.led(7, 60)
    sleep(ripple_speed)
    PYGLOW.led(7, 120)
    sleep(ripple_speed)


def rippling_confluence_3(sleep_speed):
    """
    Ripples the lights on arms 1 and 2, then arm 3
    """
    LOGGER.debug("Rippling Confluence 1...")

    ripple_speed = 0.05

    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05

    LOGGER.debug("ripple speed is: %s", ripple_speed)

    # Ripple
    # Arm 1 and 2, Red
    PYGLOW.led(1, 60)
    PYGLOW.led(7, 60)
    sleep(ripple_speed)
    PYGLOW.led(1, 120)
    PYGLOW.led(7, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Orange
    PYGLOW.led(2, 60)
    PYGLOW.led(8, 60)
    sleep(ripple_speed)
    PYGLOW.led(2, 120)
    PYGLOW.led(8, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Yellow
    PYGLOW.led(3, 60)
    PYGLOW.led(9, 60)
    sleep(ripple_speed)
    PYGLOW.led(3, 120)
    PYGLOW.led(9, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Green
    PYGLOW.led(4, 60)
    PYGLOW.led(10, 60)
    sleep(ripple_speed)
    PYGLOW.led(4, 120)
    PYGLOW.led(10, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, Blue
    PYGLOW.led(5, 60)
    PYGLOW.led(11, 60)
    sleep(ripple_speed)
    PYGLOW.led(5, 120)
    PYGLOW.led(11, 120)
    sleep(ripple_speed)
    # Arm 1 and 2, White
    PYGLOW.led(6, 60)
    PYGLOW.led(12, 60)
    sleep(ripple_speed)
    PYGLOW.led(6, 120)
    PYGLOW.led(12, 120)
    sleep(ripple_speed)
    # Arm 3, White
    PYGLOW.led(18, 60)
    sleep(ripple_speed)
    PYGLOW.led(18, 120)
    sleep(ripple_speed)
    # Arm 3, Blue
    PYGLOW.led(17, 60)
    sleep(ripple_speed)
    PYGLOW.led(17, 120)
    sleep(ripple_speed)
    # Arm 3, Green
    PYGLOW.led(16, 60)
    sleep(ripple_speed)
    PYGLOW.led(16, 120)
    sleep(ripple_speed)
    # Arm 3, Yellow
    PYGLOW.led(15, 60)
    sleep(ripple_speed)
    PYGLOW.led(15, 120)
    sleep(ripple_speed)
    # Arm 3, Orange
    PYGLOW.led(14, 60)
    sleep(ripple_speed)
    PYGLOW.led(14, 120)
    sleep(ripple_speed)
    # Arm 3, Red
    PYGLOW.led(13, 60)
    sleep(ripple_speed)
    PYGLOW.led(13, 120)
    sleep(ripple_speed)


def fading_confluence_1():
    """
    Fades the lights on arms 2 and 3, then arm 1
    """

    sleep_speed = 0.01

    # Fade Arm 2 and 3: R
    PYGLOW.led(7, 110)
    PYGLOW.led(13, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O
    PYGLOW.led(7, 100)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 110)
    PYGLOW.led(14, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y
    PYGLOW.led(7, 90)
    PYGLOW.led(13, 90)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 110)
    PYGLOW.led(15, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G
    PYGLOW.led(7, 80)
    PYGLOW.led(13, 80)
    sleep(sleep_speed)
    PYGLOW.led(8, 90)
    PYGLOW.led(14, 90)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 110)
    PYGLOW.led(16, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B
    PYGLOW.led(7, 70)
    PYGLOW.led(13, 70)
    sleep(sleep_speed)
    PYGLOW.led(8, 80)
    PYGLOW.led(14, 80)
    sleep(sleep_speed)
    PYGLOW.led(9, 90)
    PYGLOW.led(15, 90)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 110)
    PYGLOW.led(17, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W
    PYGLOW.led(7, 60)
    PYGLOW.led(13, 60)
    sleep(sleep_speed)
    PYGLOW.led(8, 70)
    PYGLOW.led(14, 70)
    sleep(sleep_speed)
    PYGLOW.led(9, 80)
    PYGLOW.led(15, 80)
    sleep(sleep_speed)
    PYGLOW.led(10, 90)
    PYGLOW.led(16, 90)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 110)
    PYGLOW.led(18, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W
    PYGLOW.led(7, 50)
    PYGLOW.led(13, 50)
    sleep(sleep_speed)
    PYGLOW.led(8, 60)
    PYGLOW.led(14, 60)
    sleep(sleep_speed)
    PYGLOW.led(9, 70)
    PYGLOW.led(15, 70)
    sleep(sleep_speed)
    PYGLOW.led(10, 80)
    PYGLOW.led(16, 80)
    sleep(sleep_speed)
    PYGLOW.led(11, 90)
    PYGLOW.led(17, 90)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W, B
    PYGLOW.led(7, 40)
    PYGLOW.led(13, 40)
    sleep(sleep_speed)
    PYGLOW.led(8, 50)
    PYGLOW.led(14, 50)
    sleep(sleep_speed)
    PYGLOW.led(9, 60)
    PYGLOW.led(15, 60)
    sleep(sleep_speed)
    PYGLOW.led(10, 70)
    PYGLOW.led(16, 70)
    sleep(sleep_speed)
    PYGLOW.led(11, 80)
    PYGLOW.led(17, 80)
    sleep(sleep_speed)
    PYGLOW.led(12, 90)
    PYGLOW.led(18, 90)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W, B, G
    PYGLOW.led(7, 30)
    PYGLOW.led(13, 30)
    sleep(sleep_speed)
    PYGLOW.led(8, 40)
    PYGLOW.led(14, 40)
    sleep(sleep_speed)
    PYGLOW.led(9, 50)
    PYGLOW.led(15, 50)
    sleep(sleep_speed)
    PYGLOW.led(10, 60)
    PYGLOW.led(16, 60)
    sleep(sleep_speed)
    PYGLOW.led(11, 70)
    PYGLOW.led(17, 70)
    sleep(sleep_speed)
    PYGLOW.led(12, 80)
    PYGLOW.led(18, 80)
    sleep(sleep_speed)
    PYGLOW.led(6, 90)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W, B, G, Y
    PYGLOW.led(7, 20)
    PYGLOW.led(13, 20)
    sleep(sleep_speed)
    PYGLOW.led(8, 30)
    PYGLOW.led(14, 30)
    sleep(sleep_speed)
    PYGLOW.led(9, 40)
    PYGLOW.led(15, 40)
    sleep(sleep_speed)
    PYGLOW.led(10, 50)
    PYGLOW.led(16, 50)
    sleep(sleep_speed)
    PYGLOW.led(11, 60)
    PYGLOW.led(17, 60)
    sleep(sleep_speed)
    PYGLOW.led(12, 70)
    PYGLOW.led(18, 70)
    sleep(sleep_speed)
    PYGLOW.led(6, 80)
    sleep(sleep_speed)
    PYGLOW.led(5, 90)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W, B, G, Y, O
    PYGLOW.led(7, 10)
    PYGLOW.led(13, 10)
    sleep(sleep_speed)
    PYGLOW.led(8, 20)
    PYGLOW.led(14, 20)
    sleep(sleep_speed)
    PYGLOW.led(9, 30)
    PYGLOW.led(15, 30)
    sleep(sleep_speed)
    PYGLOW.led(10, 40)
    PYGLOW.led(16, 40)
    sleep(sleep_speed)
    PYGLOW.led(11, 50)
    PYGLOW.led(17, 50)
    sleep(sleep_speed)
    PYGLOW.led(12, 60)
    PYGLOW.led(18, 60)
    sleep(sleep_speed)
    PYGLOW.led(6, 70)
    sleep(sleep_speed)
    PYGLOW.led(5, 80)
    sleep(sleep_speed)
    PYGLOW.led(4, 90)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: R, O, Y, G, B, W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(7, 0)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 10)
    PYGLOW.led(14, 10)
    sleep(sleep_speed)
    PYGLOW.led(9, 20)
    PYGLOW.led(15, 20)
    sleep(sleep_speed)
    PYGLOW.led(10, 30)
    PYGLOW.led(16, 30)
    sleep(sleep_speed)
    PYGLOW.led(11, 40)
    PYGLOW.led(17, 40)
    sleep(sleep_speed)
    PYGLOW.led(12, 50)
    PYGLOW.led(18, 50)
    sleep(sleep_speed)
    PYGLOW.led(6, 60)
    sleep(sleep_speed)
    PYGLOW.led(5, 70)
    sleep(sleep_speed)
    PYGLOW.led(4, 80)
    sleep(sleep_speed)
    PYGLOW.led(3, 90)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(1, 110)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: O, Y, G, B, W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(8, 0)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 10)
    PYGLOW.led(15, 10)
    sleep(sleep_speed)
    PYGLOW.led(10, 20)
    PYGLOW.led(16, 20)
    sleep(sleep_speed)
    PYGLOW.led(11, 30)
    PYGLOW.led(17, 30)
    sleep(sleep_speed)
    PYGLOW.led(12, 40)
    PYGLOW.led(18, 40)
    sleep(sleep_speed)
    PYGLOW.led(6, 50)
    sleep(sleep_speed)
    PYGLOW.led(5, 60)
    sleep(sleep_speed)
    PYGLOW.led(4, 70)
    sleep(sleep_speed)
    PYGLOW.led(3, 80)
    sleep(sleep_speed)
    PYGLOW.led(2, 90)
    sleep(sleep_speed)
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: Y, G, B, W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(9, 0)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 10)
    PYGLOW.led(16, 10)
    sleep(sleep_speed)
    PYGLOW.led(11, 20)
    PYGLOW.led(17, 20)
    sleep(sleep_speed)
    PYGLOW.led(12, 30)
    PYGLOW.led(18, 30)
    sleep(sleep_speed)
    PYGLOW.led(6, 40)
    sleep(sleep_speed)
    PYGLOW.led(5, 50)
    sleep(sleep_speed)
    PYGLOW.led(4, 60)
    sleep(sleep_speed)
    PYGLOW.led(3, 70)
    sleep(sleep_speed)
    PYGLOW.led(2, 80)
    sleep(sleep_speed)
    PYGLOW.led(1, 90)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: G, B, W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(10, 0)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 10)
    PYGLOW.led(17, 10)
    sleep(sleep_speed)
    PYGLOW.led(12, 20)
    PYGLOW.led(18, 20)
    sleep(sleep_speed)
    PYGLOW.led(6, 30)
    sleep(sleep_speed)
    PYGLOW.led(5, 40)
    sleep(sleep_speed)
    PYGLOW.led(4, 50)
    sleep(sleep_speed)
    PYGLOW.led(3, 60)
    sleep(sleep_speed)
    PYGLOW.led(2, 70)
    sleep(sleep_speed)
    PYGLOW.led(1, 80)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: B, W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(11, 0)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 10)
    PYGLOW.led(18, 10)
    sleep(sleep_speed)
    PYGLOW.led(6, 20)
    sleep(sleep_speed)
    PYGLOW.led(5, 30)
    sleep(sleep_speed)
    PYGLOW.led(4, 40)
    sleep(sleep_speed)
    PYGLOW.led(3, 50)
    sleep(sleep_speed)
    PYGLOW.led(2, 60)
    sleep(sleep_speed)
    PYGLOW.led(1, 70)
    sleep(sleep_speed)
    # Fade Arm 2 and 3: W Arm 1: W, B, G, Y, O, R
    PYGLOW.led(12, 0)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 10)
    sleep(sleep_speed)
    PYGLOW.led(5, 20)
    sleep(sleep_speed)
    PYGLOW.led(4, 30)
    sleep(sleep_speed)
    PYGLOW.led(3, 40)
    sleep(sleep_speed)
    PYGLOW.led(2, 50)
    sleep(sleep_speed)
    PYGLOW.led(1, 60)
    sleep(sleep_speed)
    # Fade Arm 1:  W, B, G, Y, O, R
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 10)
    sleep(sleep_speed)
    PYGLOW.led(4, 20)
    sleep(sleep_speed)
    PYGLOW.led(3, 30)
    sleep(sleep_speed)
    PYGLOW.led(2, 40)
    sleep(sleep_speed)
    PYGLOW.led(1, 50)
    sleep(sleep_speed)
    # Fade Arm 1: B, G, Y, O, R
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 10)
    sleep(sleep_speed)
    PYGLOW.led(3, 20)
    sleep(sleep_speed)
    PYGLOW.led(2, 30)
    sleep(sleep_speed)
    PYGLOW.led(1, 40)
    sleep(sleep_speed)
    # Fade Arm 1: G, Y, O, R
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 10)
    sleep(sleep_speed)
    PYGLOW.led(2, 20)
    sleep(sleep_speed)
    PYGLOW.led(1, 30)
    sleep(sleep_speed)
    # Fade Arm 1: Y, O, R
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 10)
    sleep(sleep_speed)
    PYGLOW.led(1, 20)
    sleep(sleep_speed)
    # Fade Arm 1: O, R
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(1, 10)
    sleep(sleep_speed)
    # Fade Arm 1: R
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    # Pause before next function
    sleep(1)


def fading_confluence_2():
    """
    Fades the lights on arms 1 and 3, then arm 2
    """

    sleep_speed = 0.01

    # Fade Arm 1 and 3: R
    PYGLOW.led(1, 110)
    PYGLOW.led(13, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O
    PYGLOW.led(1, 100)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 110)
    PYGLOW.led(14, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y
    PYGLOW.led(1, 90)
    PYGLOW.led(13, 90)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 110)
    PYGLOW.led(15, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G
    PYGLOW.led(1, 80)
    PYGLOW.led(13, 80)
    sleep(sleep_speed)
    PYGLOW.led(2, 90)
    PYGLOW.led(14, 90)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 110)
    PYGLOW.led(16, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B
    PYGLOW.led(1, 70)
    PYGLOW.led(13, 70)
    sleep(sleep_speed)
    PYGLOW.led(2, 80)
    PYGLOW.led(14, 80)
    sleep(sleep_speed)
    PYGLOW.led(3, 90)
    PYGLOW.led(15, 90)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 110)
    PYGLOW.led(17, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W
    PYGLOW.led(1, 60)
    PYGLOW.led(13, 60)
    sleep(sleep_speed)
    PYGLOW.led(2, 70)
    PYGLOW.led(14, 70)
    sleep(sleep_speed)
    PYGLOW.led(3, 80)
    PYGLOW.led(15, 80)
    sleep(sleep_speed)
    PYGLOW.led(4, 90)
    PYGLOW.led(16, 90)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 110)
    PYGLOW.led(18, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W
    PYGLOW.led(1, 50)
    PYGLOW.led(13, 50)
    sleep(sleep_speed)
    PYGLOW.led(2, 60)
    PYGLOW.led(14, 60)
    sleep(sleep_speed)
    PYGLOW.led(3, 70)
    PYGLOW.led(15, 70)
    sleep(sleep_speed)
    PYGLOW.led(4, 80)
    PYGLOW.led(16, 80)
    sleep(sleep_speed)
    PYGLOW.led(5, 90)
    PYGLOW.led(17, 90)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W, B
    PYGLOW.led(1, 40)
    PYGLOW.led(13, 40)
    sleep(sleep_speed)
    PYGLOW.led(2, 50)
    PYGLOW.led(14, 50)
    sleep(sleep_speed)
    PYGLOW.led(3, 60)
    PYGLOW.led(15, 60)
    sleep(sleep_speed)
    PYGLOW.led(4, 70)
    PYGLOW.led(16, 70)
    sleep(sleep_speed)
    PYGLOW.led(5, 80)
    PYGLOW.led(17, 80)
    sleep(sleep_speed)
    PYGLOW.led(6, 90)
    PYGLOW.led(18, 90)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W, B, G
    PYGLOW.led(1, 30)
    PYGLOW.led(13, 30)
    sleep(sleep_speed)
    PYGLOW.led(2, 40)
    PYGLOW.led(14, 40)
    sleep(sleep_speed)
    PYGLOW.led(3, 50)
    PYGLOW.led(15, 50)
    sleep(sleep_speed)
    PYGLOW.led(4, 60)
    PYGLOW.led(16, 60)
    sleep(sleep_speed)
    PYGLOW.led(5, 70)
    PYGLOW.led(17, 70)
    sleep(sleep_speed)
    PYGLOW.led(6, 80)
    PYGLOW.led(18, 80)
    sleep(sleep_speed)
    PYGLOW.led(12, 90)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W, B, G, Y
    PYGLOW.led(1, 20)
    PYGLOW.led(13, 20)
    sleep(sleep_speed)
    PYGLOW.led(2, 30)
    PYGLOW.led(14, 30)
    sleep(sleep_speed)
    PYGLOW.led(3, 40)
    PYGLOW.led(15, 40)
    sleep(sleep_speed)
    PYGLOW.led(4, 50)
    PYGLOW.led(16, 50)
    sleep(sleep_speed)
    PYGLOW.led(5, 60)
    PYGLOW.led(17, 60)
    sleep(sleep_speed)
    PYGLOW.led(6, 70)
    PYGLOW.led(18, 70)
    sleep(sleep_speed)
    PYGLOW.led(12, 80)
    sleep(sleep_speed)
    PYGLOW.led(11, 90)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W, B, G, Y, O
    PYGLOW.led(1, 10)
    PYGLOW.led(13, 10)
    sleep(sleep_speed)
    PYGLOW.led(2, 20)
    PYGLOW.led(14, 20)
    sleep(sleep_speed)
    PYGLOW.led(3, 30)
    PYGLOW.led(15, 30)
    sleep(sleep_speed)
    PYGLOW.led(4, 40)
    PYGLOW.led(16, 40)
    sleep(sleep_speed)
    PYGLOW.led(5, 50)
    PYGLOW.led(17, 50)
    sleep(sleep_speed)
    PYGLOW.led(6, 60)
    PYGLOW.led(18, 60)
    sleep(sleep_speed)
    PYGLOW.led(12, 70)
    sleep(sleep_speed)
    PYGLOW.led(11, 80)
    sleep(sleep_speed)
    PYGLOW.led(10, 90)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: R, O, Y, G, B, W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(1, 0)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 10)
    PYGLOW.led(14, 10)
    sleep(sleep_speed)
    PYGLOW.led(3, 20)
    PYGLOW.led(15, 20)
    sleep(sleep_speed)
    PYGLOW.led(4, 30)
    PYGLOW.led(16, 30)
    sleep(sleep_speed)
    PYGLOW.led(5, 40)
    PYGLOW.led(17, 40)
    sleep(sleep_speed)
    PYGLOW.led(6, 50)
    PYGLOW.led(18, 50)
    sleep(sleep_speed)
    PYGLOW.led(12, 60)
    sleep(sleep_speed)
    PYGLOW.led(11, 70)
    sleep(sleep_speed)
    PYGLOW.led(10, 80)
    sleep(sleep_speed)
    PYGLOW.led(9, 90)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(7, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: O, Y, G, B, W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(2, 0)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 10)
    PYGLOW.led(15, 10)
    sleep(sleep_speed)
    PYGLOW.led(4, 20)
    PYGLOW.led(16, 20)
    sleep(sleep_speed)
    PYGLOW.led(5, 30)
    PYGLOW.led(17, 30)
    sleep(sleep_speed)
    PYGLOW.led(6, 40)
    PYGLOW.led(18, 40)
    sleep(sleep_speed)
    PYGLOW.led(12, 50)
    sleep(sleep_speed)
    PYGLOW.led(11, 60)
    sleep(sleep_speed)
    PYGLOW.led(10, 70)
    sleep(sleep_speed)
    PYGLOW.led(9, 80)
    sleep(sleep_speed)
    PYGLOW.led(8, 90)
    sleep(sleep_speed)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: Y, G, B, W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(3, 0)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 10)
    PYGLOW.led(16, 10)
    sleep(sleep_speed)
    PYGLOW.led(5, 20)
    PYGLOW.led(17, 20)
    sleep(sleep_speed)
    PYGLOW.led(6, 30)
    PYGLOW.led(18, 30)
    sleep(sleep_speed)
    PYGLOW.led(12, 40)
    sleep(sleep_speed)
    PYGLOW.led(11, 50)
    sleep(sleep_speed)
    PYGLOW.led(10, 60)
    sleep(sleep_speed)
    PYGLOW.led(9, 70)
    sleep(sleep_speed)
    PYGLOW.led(8, 80)
    sleep(sleep_speed)
    PYGLOW.led(7, 90)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: G, B, W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(4, 0)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 10)
    PYGLOW.led(17, 10)
    sleep(sleep_speed)
    PYGLOW.led(6, 20)
    PYGLOW.led(18, 20)
    sleep(sleep_speed)
    PYGLOW.led(12, 30)
    sleep(sleep_speed)
    PYGLOW.led(11, 40)
    sleep(sleep_speed)
    PYGLOW.led(10, 50)
    sleep(sleep_speed)
    PYGLOW.led(9, 60)
    sleep(sleep_speed)
    PYGLOW.led(8, 70)
    sleep(sleep_speed)
    PYGLOW.led(7, 80)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: B, W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(5, 0)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 10)
    PYGLOW.led(18, 10)
    sleep(sleep_speed)
    PYGLOW.led(12, 20)
    sleep(sleep_speed)
    PYGLOW.led(11, 30)
    sleep(sleep_speed)
    PYGLOW.led(10, 40)
    sleep(sleep_speed)
    PYGLOW.led(9, 50)
    sleep(sleep_speed)
    PYGLOW.led(8, 60)
    sleep(sleep_speed)
    PYGLOW.led(7, 70)
    sleep(sleep_speed)
    # Fade Arm 1 and 3: W Arm 2: W, B, G, Y, O, R
    PYGLOW.led(6, 0)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 10)
    sleep(sleep_speed)
    PYGLOW.led(11, 20)
    sleep(sleep_speed)
    PYGLOW.led(10, 30)
    sleep(sleep_speed)
    PYGLOW.led(9, 40)
    sleep(sleep_speed)
    PYGLOW.led(8, 50)
    sleep(sleep_speed)
    PYGLOW.led(7, 60)
    sleep(sleep_speed)
    # Fade Arm 2:  W, B, G, Y, O, R
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 10)
    sleep(sleep_speed)
    PYGLOW.led(10, 20)
    sleep(sleep_speed)
    PYGLOW.led(9, 30)
    sleep(sleep_speed)
    PYGLOW.led(8, 40)
    sleep(sleep_speed)
    PYGLOW.led(7, 50)
    sleep(sleep_speed)
    # Fade Arm 2: B, G, Y, O, R
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 10)
    sleep(sleep_speed)
    PYGLOW.led(9, 20)
    sleep(sleep_speed)
    PYGLOW.led(8, 30)
    sleep(sleep_speed)
    PYGLOW.led(7, 40)
    sleep(sleep_speed)
    # Fade Arm 2: G, Y, O, R
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 10)
    sleep(sleep_speed)
    PYGLOW.led(8, 20)
    sleep(sleep_speed)
    PYGLOW.led(7, 30)
    sleep(sleep_speed)
    # Fade Arm 2: Y, O, R
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 10)
    sleep(sleep_speed)
    PYGLOW.led(7, 20)
    sleep(sleep_speed)
    # Fade Arm 2: O, R
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(7, 10)
    sleep(sleep_speed)
    # Fade Arm 2: R
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Pause before next function
    sleep(1)


def fading_confluence_3():
    """
    Fades the lights on arms 1 and 2, then arm 3
    """

    sleep_speed = 0.01

    # Fade Arm 1 and 2: R
    PYGLOW.led(1, 110)
    PYGLOW.led(7, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O
    PYGLOW.led(1, 100)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 110)
    PYGLOW.led(8, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y
    PYGLOW.led(1, 90)
    PYGLOW.led(7, 90)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 110)
    PYGLOW.led(9, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G
    PYGLOW.led(1, 80)
    PYGLOW.led(7, 80)
    sleep(sleep_speed)
    PYGLOW.led(2, 90)
    PYGLOW.led(8, 90)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 110)
    PYGLOW.led(10, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B
    PYGLOW.led(1, 70)
    PYGLOW.led(7, 70)
    sleep(sleep_speed)
    PYGLOW.led(2, 80)
    PYGLOW.led(8, 80)
    sleep(sleep_speed)
    PYGLOW.led(3, 90)
    PYGLOW.led(9, 90)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 110)
    PYGLOW.led(11, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W
    PYGLOW.led(1, 60)
    PYGLOW.led(7, 60)
    sleep(sleep_speed)
    PYGLOW.led(2, 70)
    PYGLOW.led(8, 70)
    sleep(sleep_speed)
    PYGLOW.led(3, 80)
    PYGLOW.led(9, 80)
    sleep(sleep_speed)
    PYGLOW.led(4, 90)
    PYGLOW.led(10, 90)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 110)
    PYGLOW.led(12, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W
    PYGLOW.led(1, 50)
    PYGLOW.led(7, 50)
    sleep(sleep_speed)
    PYGLOW.led(2, 60)
    PYGLOW.led(8, 60)
    sleep(sleep_speed)
    PYGLOW.led(3, 70)
    PYGLOW.led(9, 70)
    sleep(sleep_speed)
    PYGLOW.led(4, 80)
    PYGLOW.led(10, 80)
    sleep(sleep_speed)
    PYGLOW.led(5, 90)
    PYGLOW.led(11, 90)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W, B
    PYGLOW.led(1, 40)
    PYGLOW.led(7, 40)
    sleep(sleep_speed)
    PYGLOW.led(2, 50)
    PYGLOW.led(8, 50)
    sleep(sleep_speed)
    PYGLOW.led(3, 60)
    PYGLOW.led(9, 60)
    sleep(sleep_speed)
    PYGLOW.led(4, 70)
    PYGLOW.led(10, 70)
    sleep(sleep_speed)
    PYGLOW.led(5, 80)
    PYGLOW.led(11, 80)
    sleep(sleep_speed)
    PYGLOW.led(6, 90)
    PYGLOW.led(12, 90)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W, B, G
    PYGLOW.led(1, 30)
    PYGLOW.led(7, 30)
    sleep(sleep_speed)
    PYGLOW.led(2, 40)
    PYGLOW.led(8, 40)
    sleep(sleep_speed)
    PYGLOW.led(3, 50)
    PYGLOW.led(9, 50)
    sleep(sleep_speed)
    PYGLOW.led(4, 60)
    PYGLOW.led(10, 60)
    sleep(sleep_speed)
    PYGLOW.led(5, 70)
    PYGLOW.led(11, 70)
    sleep(sleep_speed)
    PYGLOW.led(6, 80)
    PYGLOW.led(12, 80)
    sleep(sleep_speed)
    PYGLOW.led(18, 90)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W, B, G, Y
    PYGLOW.led(1, 20)
    PYGLOW.led(7, 20)
    sleep(sleep_speed)
    PYGLOW.led(2, 30)
    PYGLOW.led(8, 30)
    sleep(sleep_speed)
    PYGLOW.led(3, 40)
    PYGLOW.led(9, 40)
    sleep(sleep_speed)
    PYGLOW.led(4, 50)
    PYGLOW.led(10, 50)
    sleep(sleep_speed)
    PYGLOW.led(5, 60)
    PYGLOW.led(11, 60)
    sleep(sleep_speed)
    PYGLOW.led(6, 70)
    PYGLOW.led(12, 70)
    sleep(sleep_speed)
    PYGLOW.led(18, 80)
    sleep(sleep_speed)
    PYGLOW.led(17, 90)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W, B, G, Y, O
    PYGLOW.led(1, 10)
    PYGLOW.led(7, 10)
    sleep(sleep_speed)
    PYGLOW.led(2, 20)
    PYGLOW.led(8, 20)
    sleep(sleep_speed)
    PYGLOW.led(3, 30)
    PYGLOW.led(9, 30)
    sleep(sleep_speed)
    PYGLOW.led(4, 40)
    PYGLOW.led(10, 40)
    sleep(sleep_speed)
    PYGLOW.led(5, 50)
    PYGLOW.led(11, 50)
    sleep(sleep_speed)
    PYGLOW.led(6, 60)
    PYGLOW.led(12, 60)
    sleep(sleep_speed)
    PYGLOW.led(18, 70)
    sleep(sleep_speed)
    PYGLOW.led(17, 80)
    sleep(sleep_speed)
    PYGLOW.led(16, 90)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: R, O, Y, G, B, W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(1, 0)
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 10)
    PYGLOW.led(8, 10)
    sleep(sleep_speed)
    PYGLOW.led(3, 20)
    PYGLOW.led(9, 20)
    sleep(sleep_speed)
    PYGLOW.led(4, 30)
    PYGLOW.led(10, 30)
    sleep(sleep_speed)
    PYGLOW.led(5, 40)
    PYGLOW.led(11, 40)
    sleep(sleep_speed)
    PYGLOW.led(6, 50)
    PYGLOW.led(12, 50)
    sleep(sleep_speed)
    PYGLOW.led(18, 60)
    sleep(sleep_speed)
    PYGLOW.led(17, 70)
    sleep(sleep_speed)
    PYGLOW.led(16, 80)
    sleep(sleep_speed)
    PYGLOW.led(15, 90)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(13, 110)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: O, Y, G, B, W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(2, 0)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 10)
    PYGLOW.led(9, 10)
    sleep(sleep_speed)
    PYGLOW.led(4, 20)
    PYGLOW.led(10, 20)
    sleep(sleep_speed)
    PYGLOW.led(5, 30)
    PYGLOW.led(11, 30)
    sleep(sleep_speed)
    PYGLOW.led(6, 40)
    PYGLOW.led(12, 40)
    sleep(sleep_speed)
    PYGLOW.led(18, 50)
    sleep(sleep_speed)
    PYGLOW.led(17, 60)
    sleep(sleep_speed)
    PYGLOW.led(16, 70)
    sleep(sleep_speed)
    PYGLOW.led(15, 80)
    sleep(sleep_speed)
    PYGLOW.led(14, 90)
    sleep(sleep_speed)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: Y, G, B, W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(3, 0)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 10)
    PYGLOW.led(10, 10)
    sleep(sleep_speed)
    PYGLOW.led(5, 20)
    PYGLOW.led(11, 20)
    sleep(sleep_speed)
    PYGLOW.led(6, 30)
    PYGLOW.led(12, 30)
    sleep(sleep_speed)
    PYGLOW.led(18, 40)
    sleep(sleep_speed)
    PYGLOW.led(17, 50)
    sleep(sleep_speed)
    PYGLOW.led(16, 60)
    sleep(sleep_speed)
    PYGLOW.led(15, 70)
    sleep(sleep_speed)
    PYGLOW.led(14, 80)
    sleep(sleep_speed)
    PYGLOW.led(13, 90)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: G, B, W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(4, 0)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 10)
    PYGLOW.led(11, 10)
    sleep(sleep_speed)
    PYGLOW.led(6, 20)
    PYGLOW.led(12, 20)
    sleep(sleep_speed)
    PYGLOW.led(18, 30)
    sleep(sleep_speed)
    PYGLOW.led(17, 40)
    sleep(sleep_speed)
    PYGLOW.led(16, 50)
    sleep(sleep_speed)
    PYGLOW.led(15, 60)
    sleep(sleep_speed)
    PYGLOW.led(14, 70)
    sleep(sleep_speed)
    PYGLOW.led(13, 80)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: B, W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(5, 0)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 10)
    PYGLOW.led(12, 10)
    sleep(sleep_speed)
    PYGLOW.led(18, 20)
    sleep(sleep_speed)
    PYGLOW.led(17, 30)
    sleep(sleep_speed)
    PYGLOW.led(16, 40)
    sleep(sleep_speed)
    PYGLOW.led(15, 50)
    sleep(sleep_speed)
    PYGLOW.led(14, 60)
    sleep(sleep_speed)
    PYGLOW.led(13, 70)
    sleep(sleep_speed)
    # Fade Arm 1 and 2: W Arm 3: W, B, G, Y, O, R
    PYGLOW.led(6, 0)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 10)
    sleep(sleep_speed)
    PYGLOW.led(17, 20)
    sleep(sleep_speed)
    PYGLOW.led(16, 30)
    sleep(sleep_speed)
    PYGLOW.led(15, 40)
    sleep(sleep_speed)
    PYGLOW.led(14, 50)
    sleep(sleep_speed)
    PYGLOW.led(13, 60)
    sleep(sleep_speed)
    # Fade Arm 3:  W, B, G, Y, O, R
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 10)
    sleep(sleep_speed)
    PYGLOW.led(16, 20)
    sleep(sleep_speed)
    PYGLOW.led(15, 30)
    sleep(sleep_speed)
    PYGLOW.led(14, 40)
    sleep(sleep_speed)
    PYGLOW.led(13, 50)
    sleep(sleep_speed)
    # Fade Arm 3: B, G, Y, O, R
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 10)
    sleep(sleep_speed)
    PYGLOW.led(15, 20)
    sleep(sleep_speed)
    PYGLOW.led(14, 30)
    sleep(sleep_speed)
    PYGLOW.led(13, 40)
    sleep(sleep_speed)
    # Fade Arm 3: G, Y, O, R
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 10)
    sleep(sleep_speed)
    PYGLOW.led(14, 20)
    sleep(sleep_speed)
    PYGLOW.led(13, 30)
    sleep(sleep_speed)
    # Fade Arm 3: Y, O, R
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 10)
    sleep(sleep_speed)
    PYGLOW.led(13, 20)
    sleep(sleep_speed)
    # Fade Arm 3: O, R
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(13, 10)
    sleep(sleep_speed)
    # Fade Arm 3: R
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Pause before next function
    sleep(1)


def confluence_slow():
    """
    Gradually increases the speed at which the LEDs light up
    """
    LOGGER.debug("Confluence slow")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05


def confluence_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("sleep_speed = %s", sleep_speed)
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025


def main():
    """
    The main function
    """
    LOGGER.debug("START")

    confluence_slow()
    confluence_fast()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/rippling_fading_confluence.log'
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
