#!/usr/bin/env python3
"""
Fading Spiral Arms

This program lights up the LEDs on arm 1 one at at time,
then arm 2, then arm 3. Instead the lights being turned off
at a time like in the Spiral Arms program, the lights
gradually fade.

....................

Functions:
- fading_sprial_arms: fades the spiral arms
- run_10_times: Runs a function 10 times


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


def run_10_times(function_name):
    """
    This program will run a fuction 10 times.
    
    Argument: 
        - function_name
    """
    LOGGER.debug("Running 10 times...")

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("Running number %s", i)
        function_name()


def fading_spiral_arms():
    """ Fades the spiral arms """
    LOGGER.debug("Fading spiral arms...")

    sleep_speed = 0.01

    # Turn LED 1
    PYGLOW.led(1, 180)
    sleep(sleep_speed)
    # Turn on LED 2
    PYGLOW.led(2, 180)
    sleep(sleep_speed)
    # Fade LED 1
    PYGLOW.led(1, 170)
    sleep(sleep_speed)
    # Turn on LED 3
    PYGLOW.led(3, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 2
    PYGLOW.led(1, 160)
    sleep(sleep_speed)
    PYGLOW.led(2, 170)
    sleep(sleep_speed)
    # Turn on LED 4
    PYGLOW.led(4, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 3
    PYGLOW.led(1, 150)
    sleep(sleep_speed)
    PYGLOW.led(2, 160)
    sleep(sleep_speed)
    PYGLOW.led(3, 170)
    sleep(sleep_speed)
    # Turn on LED 5
    PYGLOW.led(5, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 4
    PYGLOW.led(1, 140)
    sleep(sleep_speed)
    PYGLOW.led(2, 150)
    sleep(sleep_speed)
    PYGLOW.led(3, 160)
    sleep(sleep_speed)
    PYGLOW.led(4, 170)
    sleep(sleep_speed)
    # Turn on LED 6
    PYGLOW.led(6, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 5
    PYGLOW.led(1, 130)
    sleep(sleep_speed)
    PYGLOW.led(2, 140)
    sleep(sleep_speed)
    PYGLOW.led(3, 150)
    sleep(sleep_speed)
    PYGLOW.led(4, 160)
    sleep(sleep_speed)
    PYGLOW.led(5, 170)
    sleep(sleep_speed)
    # Turn on LED 7
    PYGLOW.led(7, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 5
    PYGLOW.led(1, 120)
    sleep(sleep_speed)
    PYGLOW.led(2, 130)
    sleep(sleep_speed)
    PYGLOW.led(3, 140)
    sleep(sleep_speed)
    PYGLOW.led(4, 150)
    sleep(sleep_speed)
    PYGLOW.led(5, 160)
    sleep(sleep_speed)
    PYGLOW.led(6, 170)
    sleep(sleep_speed)
    # Turn on LED 8
    PYGLOW.led(8, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 7
    PYGLOW.led(1, 110)
    sleep(sleep_speed)
    PYGLOW.led(2, 120)
    sleep(sleep_speed)
    PYGLOW.led(3, 130)
    sleep(sleep_speed)
    PYGLOW.led(4, 140)
    sleep(sleep_speed)
    PYGLOW.led(5, 150)
    sleep(sleep_speed)
    PYGLOW.led(6, 160)
    sleep(sleep_speed)
    PYGLOW.led(7, 170)
    sleep(sleep_speed)
    # Turn on LED 9
    PYGLOW.led(9, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 8
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 110)
    sleep(sleep_speed)
    PYGLOW.led(3, 120)
    sleep(sleep_speed)
    PYGLOW.led(4, 130)
    sleep(sleep_speed)
    PYGLOW.led(5, 140)
    sleep(sleep_speed)
    PYGLOW.led(6, 150)
    sleep(sleep_speed)
    PYGLOW.led(7, 160)
    sleep(sleep_speed)
    PYGLOW.led(8, 170)
    sleep(sleep_speed)
    # Turn on LED 10
    PYGLOW.led(10, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 9
    PYGLOW.led(1, 90)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 110)
    sleep(sleep_speed)
    PYGLOW.led(4, 120)
    sleep(sleep_speed)
    PYGLOW.led(5, 130)
    sleep(sleep_speed)
    PYGLOW.led(6, 140)
    sleep(sleep_speed)
    PYGLOW.led(7, 150)
    sleep(sleep_speed)
    PYGLOW.led(8, 160)
    sleep(sleep_speed)
    PYGLOW.led(9, 170)
    sleep(sleep_speed)
    # Turn on LED 11
    PYGLOW.led(11, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 10
    PYGLOW.led(1, 80)
    sleep(sleep_speed)
    PYGLOW.led(2, 90)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 110)
    sleep(sleep_speed)
    PYGLOW.led(5, 120)
    sleep(sleep_speed)
    PYGLOW.led(6, 130)
    sleep(sleep_speed)
    PYGLOW.led(7, 140)
    sleep(sleep_speed)
    PYGLOW.led(8, 150)
    sleep(sleep_speed)
    PYGLOW.led(9, 160)
    sleep(sleep_speed)
    PYGLOW.led(10, 170)
    sleep(sleep_speed)
    # Turn on LED 12
    PYGLOW.led(12, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 11
    PYGLOW.led(1, 70)
    sleep(sleep_speed)
    PYGLOW.led(2, 80)
    sleep(sleep_speed)
    PYGLOW.led(3, 90)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 110)
    sleep(sleep_speed)
    PYGLOW.led(6, 120)
    sleep(sleep_speed)
    PYGLOW.led(7, 130)
    sleep(sleep_speed)
    PYGLOW.led(8, 140)
    sleep(sleep_speed)
    PYGLOW.led(9, 150)
    sleep(sleep_speed)
    PYGLOW.led(10, 160)
    sleep(sleep_speed)
    PYGLOW.led(11, 170)
    sleep(sleep_speed)
    # Turn on LED 13
    PYGLOW.led(13, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 12
    PYGLOW.led(1, 60)
    sleep(sleep_speed)
    PYGLOW.led(2, 70)
    sleep(sleep_speed)
    PYGLOW.led(3, 80)
    sleep(sleep_speed)
    PYGLOW.led(4, 90)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 110)
    sleep(sleep_speed)
    PYGLOW.led(7, 120)
    sleep(sleep_speed)
    PYGLOW.led(8, 130)
    sleep(sleep_speed)
    PYGLOW.led(9, 140)
    sleep(sleep_speed)
    PYGLOW.led(10, 150)
    sleep(sleep_speed)
    PYGLOW.led(11, 160)
    sleep(sleep_speed)
    PYGLOW.led(12, 170)
    sleep(sleep_speed)
    # Turn on LED 14
    PYGLOW.led(14, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 13
    PYGLOW.led(1, 50)
    sleep(sleep_speed)
    PYGLOW.led(2, 60)
    sleep(sleep_speed)
    PYGLOW.led(3, 70)
    sleep(sleep_speed)
    PYGLOW.led(4, 80)
    sleep(sleep_speed)
    PYGLOW.led(5, 90)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(7, 110)
    sleep(sleep_speed)
    PYGLOW.led(8, 120)
    sleep(sleep_speed)
    PYGLOW.led(9, 130)
    sleep(sleep_speed)
    PYGLOW.led(10, 140)
    sleep(sleep_speed)
    PYGLOW.led(11, 150)
    sleep(sleep_speed)
    PYGLOW.led(12, 160)
    sleep(sleep_speed)
    PYGLOW.led(13, 170)
    sleep(sleep_speed)
    # Turn on LED 15
    PYGLOW.led(15, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 14
    PYGLOW.led(1, 40)
    sleep(sleep_speed)
    PYGLOW.led(2, 50)
    sleep(sleep_speed)
    PYGLOW.led(3, 60)
    sleep(sleep_speed)
    PYGLOW.led(4, 70)
    sleep(sleep_speed)
    PYGLOW.led(5, 80)
    sleep(sleep_speed)
    PYGLOW.led(6, 90)
    sleep(sleep_speed)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 110)
    sleep(sleep_speed)
    PYGLOW.led(9, 120)
    sleep(sleep_speed)
    PYGLOW.led(10, 130)
    sleep(sleep_speed)
    PYGLOW.led(11, 140)
    sleep(sleep_speed)
    PYGLOW.led(12, 150)
    sleep(sleep_speed)
    PYGLOW.led(13, 160)
    sleep(sleep_speed)
    PYGLOW.led(14, 170)
    sleep(sleep_speed)
    # Turn on LED 16
    PYGLOW.led(16, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 15
    PYGLOW.led(1, 30)
    sleep(sleep_speed)
    PYGLOW.led(2, 40)
    sleep(sleep_speed)
    PYGLOW.led(3, 50)
    sleep(sleep_speed)
    PYGLOW.led(4, 60)
    sleep(sleep_speed)
    PYGLOW.led(5, 70)
    sleep(sleep_speed)
    PYGLOW.led(6, 80)
    sleep(sleep_speed)
    PYGLOW.led(7, 90)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 110)
    sleep(sleep_speed)
    PYGLOW.led(10, 120)
    sleep(sleep_speed)
    PYGLOW.led(11, 130)
    sleep(sleep_speed)
    PYGLOW.led(12, 140)
    sleep(sleep_speed)
    PYGLOW.led(13, 150)
    sleep(sleep_speed)
    PYGLOW.led(14, 160)
    sleep(sleep_speed)
    PYGLOW.led(15, 170)
    sleep(sleep_speed)
    # Turn on LED 17
    PYGLOW.led(17, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 16
    PYGLOW.led(1, 20)
    sleep(sleep_speed)
    PYGLOW.led(2, 30)
    sleep(sleep_speed)
    PYGLOW.led(3, 40)
    sleep(sleep_speed)
    PYGLOW.led(4, 50)
    sleep(sleep_speed)
    PYGLOW.led(5, 60)
    sleep(sleep_speed)
    PYGLOW.led(6, 70)
    sleep(sleep_speed)
    PYGLOW.led(7, 80)
    sleep(sleep_speed)
    PYGLOW.led(8, 90)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 110)
    sleep(sleep_speed)
    PYGLOW.led(11, 120)
    sleep(sleep_speed)
    PYGLOW.led(12, 130)
    sleep(sleep_speed)
    PYGLOW.led(13, 140)
    sleep(sleep_speed)
    PYGLOW.led(14, 150)
    sleep(sleep_speed)
    PYGLOW.led(15, 160)
    sleep(sleep_speed)
    PYGLOW.led(16, 170)
    sleep(sleep_speed)
    # Turn on LED 18
    PYGLOW.led(18, 180)
    sleep(sleep_speed)
    # Fade LED 1 - 17
    PYGLOW.led(1, 10)
    sleep(sleep_speed)
    PYGLOW.led(2, 20)
    sleep(sleep_speed)
    PYGLOW.led(3, 30)
    sleep(sleep_speed)
    PYGLOW.led(4, 40)
    sleep(sleep_speed)
    PYGLOW.led(5, 50)
    sleep(sleep_speed)
    PYGLOW.led(6, 60)
    sleep(sleep_speed)
    PYGLOW.led(7, 70)
    sleep(sleep_speed)
    PYGLOW.led(8, 80)
    sleep(sleep_speed)
    PYGLOW.led(9, 90)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 110)
    sleep(sleep_speed)
    PYGLOW.led(12, 120)
    sleep(sleep_speed)
    PYGLOW.led(13, 130)
    sleep(sleep_speed)
    PYGLOW.led(14, 140)
    sleep(sleep_speed)
    PYGLOW.led(15, 150)
    sleep(sleep_speed)
    PYGLOW.led(16, 160)
    sleep(sleep_speed)
    PYGLOW.led(17, 170)
    sleep(sleep_speed)
    # Fade LED 1 - 18
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 10)
    sleep(sleep_speed)
    PYGLOW.led(3, 20)
    sleep(sleep_speed)
    PYGLOW.led(4, 30)
    sleep(sleep_speed)
    PYGLOW.led(5, 40)
    sleep(sleep_speed)
    PYGLOW.led(6, 50)
    sleep(sleep_speed)
    PYGLOW.led(7, 60)
    sleep(sleep_speed)
    PYGLOW.led(8, 70)
    sleep(sleep_speed)
    PYGLOW.led(9, 80)
    sleep(sleep_speed)
    PYGLOW.led(10, 90)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 110)
    sleep(sleep_speed)
    PYGLOW.led(13, 120)
    sleep(sleep_speed)
    PYGLOW.led(14, 130)
    sleep(sleep_speed)
    PYGLOW.led(15, 140)
    sleep(sleep_speed)
    PYGLOW.led(16, 150)
    sleep(sleep_speed)
    PYGLOW.led(17, 160)
    sleep(sleep_speed)
    PYGLOW.led(18, 170)
    sleep(sleep_speed)
    # Fade LED 2 - 18
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 10)
    sleep(sleep_speed)
    PYGLOW.led(4, 20)
    sleep(sleep_speed)
    PYGLOW.led(5, 30)
    sleep(sleep_speed)
    PYGLOW.led(6, 40)
    sleep(sleep_speed)
    PYGLOW.led(7, 50)
    sleep(sleep_speed)
    PYGLOW.led(8, 60)
    sleep(sleep_speed)
    PYGLOW.led(9, 70)
    sleep(sleep_speed)
    PYGLOW.led(10, 80)
    sleep(sleep_speed)
    PYGLOW.led(11, 90)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(13, 110)
    sleep(sleep_speed)
    PYGLOW.led(14, 120)
    sleep(sleep_speed)
    PYGLOW.led(15, 130)
    sleep(sleep_speed)
    PYGLOW.led(16, 140)
    sleep(sleep_speed)
    PYGLOW.led(17, 150)
    sleep(sleep_speed)
    PYGLOW.led(18, 160)
    sleep(sleep_speed)
    # Fade LED 3 - 18
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 10)
    sleep(sleep_speed)
    PYGLOW.led(5, 20)
    sleep(sleep_speed)
    PYGLOW.led(6, 30)
    sleep(sleep_speed)
    PYGLOW.led(7, 40)
    sleep(sleep_speed)
    PYGLOW.led(8, 50)
    sleep(sleep_speed)
    PYGLOW.led(9, 60)
    sleep(sleep_speed)
    PYGLOW.led(10, 70)
    sleep(sleep_speed)
    PYGLOW.led(11, 80)
    sleep(sleep_speed)
    PYGLOW.led(12, 90)
    sleep(sleep_speed)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 110)
    sleep(sleep_speed)
    PYGLOW.led(15, 120)
    sleep(sleep_speed)
    PYGLOW.led(16, 130)
    sleep(sleep_speed)
    PYGLOW.led(17, 140)
    sleep(sleep_speed)
    PYGLOW.led(18, 150)
    sleep(sleep_speed)
    # Fade LED 4 - 18
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 10)
    sleep(sleep_speed)
    PYGLOW.led(6, 20)
    sleep(sleep_speed)
    PYGLOW.led(7, 30)
    sleep(sleep_speed)
    PYGLOW.led(8, 40)
    sleep(sleep_speed)
    PYGLOW.led(9, 50)
    sleep(sleep_speed)
    PYGLOW.led(10, 60)
    sleep(sleep_speed)
    PYGLOW.led(11, 70)
    sleep(sleep_speed)
    PYGLOW.led(12, 80)
    sleep(sleep_speed)
    PYGLOW.led(13, 90)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 110)
    sleep(sleep_speed)
    PYGLOW.led(16, 120)
    sleep(sleep_speed)
    PYGLOW.led(17, 130)
    sleep(sleep_speed)
    PYGLOW.led(18, 140)
    sleep(sleep_speed)
    # Fade LED 5 - 18
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 10)
    sleep(sleep_speed)
    PYGLOW.led(7, 20)
    sleep(sleep_speed)
    PYGLOW.led(8, 30)
    sleep(sleep_speed)
    PYGLOW.led(9, 40)
    sleep(sleep_speed)
    PYGLOW.led(10, 50)
    sleep(sleep_speed)
    PYGLOW.led(11, 60)
    sleep(sleep_speed)
    PYGLOW.led(12, 70)
    sleep(sleep_speed)
    PYGLOW.led(13, 80)
    sleep(sleep_speed)
    PYGLOW.led(14, 90)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 110)
    sleep(sleep_speed)
    PYGLOW.led(17, 120)
    sleep(sleep_speed)
    PYGLOW.led(18, 130)
    sleep(sleep_speed)
    # Fade LED 6 - 18
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(7, 10)
    sleep(sleep_speed)
    PYGLOW.led(8, 20)
    sleep(sleep_speed)
    PYGLOW.led(9, 30)
    sleep(sleep_speed)
    PYGLOW.led(10, 40)
    sleep(sleep_speed)
    PYGLOW.led(11, 50)
    sleep(sleep_speed)
    PYGLOW.led(12, 60)
    sleep(sleep_speed)
    PYGLOW.led(13, 70)
    sleep(sleep_speed)
    PYGLOW.led(14, 80)
    sleep(sleep_speed)
    PYGLOW.led(15, 90)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 110)
    sleep(sleep_speed)
    PYGLOW.led(18, 120)
    sleep(sleep_speed)
    # Fade LED 7 - 18
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 10)
    sleep(sleep_speed)
    PYGLOW.led(9, 20)
    sleep(sleep_speed)
    PYGLOW.led(10, 30)
    sleep(sleep_speed)
    PYGLOW.led(11, 40)
    sleep(sleep_speed)
    PYGLOW.led(12, 50)
    sleep(sleep_speed)
    PYGLOW.led(13, 60)
    sleep(sleep_speed)
    PYGLOW.led(14, 70)
    sleep(sleep_speed)
    PYGLOW.led(15, 80)
    sleep(sleep_speed)
    PYGLOW.led(16, 90)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 110)
    sleep(sleep_speed)
    # Fade LED 8 - 18
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 10)
    sleep(sleep_speed)
    PYGLOW.led(10, 20)
    sleep(sleep_speed)
    PYGLOW.led(11, 30)
    sleep(sleep_speed)
    PYGLOW.led(12, 40)
    sleep(sleep_speed)
    PYGLOW.led(13, 50)
    sleep(sleep_speed)
    PYGLOW.led(14, 60)
    sleep(sleep_speed)
    PYGLOW.led(15, 70)
    sleep(sleep_speed)
    PYGLOW.led(16, 80)
    sleep(sleep_speed)
    PYGLOW.led(17, 90)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    # Fade LED 9 - 18
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 10)
    sleep(sleep_speed)
    PYGLOW.led(11, 20)
    sleep(sleep_speed)
    PYGLOW.led(12, 30)
    sleep(sleep_speed)
    PYGLOW.led(13, 40)
    sleep(sleep_speed)
    PYGLOW.led(14, 50)
    sleep(sleep_speed)
    PYGLOW.led(15, 60)
    sleep(sleep_speed)
    PYGLOW.led(16, 70)
    sleep(sleep_speed)
    PYGLOW.led(17, 80)
    sleep(sleep_speed)
    PYGLOW.led(18, 90)
    sleep(sleep_speed)
    # Fade LED 10 - 18
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 10)
    sleep(sleep_speed)
    PYGLOW.led(12, 20)
    sleep(sleep_speed)
    PYGLOW.led(13, 30)
    sleep(sleep_speed)
    PYGLOW.led(14, 40)
    sleep(sleep_speed)
    PYGLOW.led(15, 50)
    sleep(sleep_speed)
    PYGLOW.led(16, 60)
    sleep(sleep_speed)
    PYGLOW.led(17, 70)
    sleep(sleep_speed)
    PYGLOW.led(18, 80)
    sleep(sleep_speed)
    # Fade LED 11 - 18
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 10)
    sleep(sleep_speed)
    PYGLOW.led(13, 20)
    sleep(sleep_speed)
    PYGLOW.led(14, 30)
    sleep(sleep_speed)
    PYGLOW.led(15, 40)
    sleep(sleep_speed)
    PYGLOW.led(16, 50)
    sleep(sleep_speed)
    PYGLOW.led(17, 60)
    sleep(sleep_speed)
    PYGLOW.led(18, 70)
    sleep(sleep_speed)
    # Fade LED 12 - 18
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(13, 10)
    sleep(sleep_speed)
    PYGLOW.led(14, 20)
    sleep(sleep_speed)
    PYGLOW.led(15, 30)
    sleep(sleep_speed)
    PYGLOW.led(16, 40)
    sleep(sleep_speed)
    PYGLOW.led(17, 50)
    sleep(sleep_speed)
    PYGLOW.led(18, 60)
    sleep(sleep_speed)
    # Fade LED 13 - 18
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 10)
    sleep(sleep_speed)
    PYGLOW.led(15, 20)
    sleep(sleep_speed)
    PYGLOW.led(16, 30)
    sleep(sleep_speed)
    PYGLOW.led(17, 40)
    sleep(sleep_speed)
    PYGLOW.led(18, 50)
    sleep(sleep_speed)
    # Fade LED 14 - 18
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 10)
    sleep(sleep_speed)
    PYGLOW.led(16, 20)
    sleep(sleep_speed)
    PYGLOW.led(17, 30)
    sleep(sleep_speed)
    PYGLOW.led(18, 40)
    sleep(sleep_speed)
    # Fade LED 15 - 18
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 10)
    sleep(sleep_speed)
    PYGLOW.led(17, 20)
    sleep(sleep_speed)
    PYGLOW.led(18, 30)
    sleep(sleep_speed)
    # Fade LED 16 - 18
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 10)
    sleep(sleep_speed)
    PYGLOW.led(18, 20)
    sleep(sleep_speed)
    # Fade LED 17 and 18
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 10)
    sleep(sleep_speed)
    # Fade LED 18
    PYGLOW.led(18, 0)
    sleep(sleep_speed)


def main():
    """
    This is the main function.
    """
    LOGGER.debug("START")
    run_10_times(function_name=fading_spiral_arms)
    LOGGER.debug("END")
    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exits.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/03_fading_spiral_arms.log'
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
