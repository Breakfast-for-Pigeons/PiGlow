#!/usr/bin/env python3
"""
Meteor Shower with Fireballs

This program lights up the LEDs on arm 1 one at at time then
then fades them. Then arm 2. Then arm 3. The code is the
same as the Meteor Shower program, except it randomizes the
brightness of the white LEDs. If the brightness of the white
LED is greater than 250, it is considered a fireball meteor
and will print a message to the screen saying "Fireball!"

....................

Functions:
- shooting_star_1: lights up the LEDs on arm 1 one at a time and
                   then fades them.
- shooting_star_2: lights up the LEDs on arm 2 one at a time and
                   then fades them.
- shooting_star_3: lights up the LEDs on arm 3 one at a time and
                   then fades them.
- random_brightness: returns a random number between 0 and 255

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

import random
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


def random_brightness():
    """
    Returns a random number between 0 and 255
    """
    return random.randint(0, 255)


def shooting_star_1():
    ''' Turn on Arm 1 LEDS and fade '''
    LOGGER.debug("Shooting Star 1")

    sleep_speed = 0.01

    # Turn on A1L1
    PYGLOW.led(1, 60)
    sleep(sleep_speed)
    # Turn on A1L2
    PYGLOW.led(2, 60)
    sleep(sleep_speed)
    # Fade A1L1
    PYGLOW.led(1, 50)
    sleep(sleep_speed)
    # Turn on A1L3
    PYGLOW.led(3, 60)
    sleep(sleep_speed)
    # Fade A1L1 - 2
    PYGLOW.led(1, 40)
    sleep(sleep_speed)
    PYGLOW.led(2, 50)
    sleep(sleep_speed)
    # Turn on A1L4
    PYGLOW.led(4, 60)
    sleep(sleep_speed)
    # Fade A1L1 - 3
    PYGLOW.led(1, 30)
    sleep(sleep_speed)
    PYGLOW.led(2, 40)
    sleep(sleep_speed)
    PYGLOW.led(3, 50)
    sleep(sleep_speed)
    # Turn on A1L5
    PYGLOW.led(5, 60)
    sleep(sleep_speed)
    # Fade A1L1 - 4
    PYGLOW.led(1, 20)
    sleep(sleep_speed)
    PYGLOW.led(2, 30)
    sleep(sleep_speed)
    PYGLOW.led(3, 40)
    sleep(sleep_speed)
    PYGLOW.led(4, 50)
    sleep(sleep_speed)
    # Turn on A1L6, get random brightness
    brightness = random_brightness()
    PYGLOW.led(6, brightness)
    if brightness > 250:
        print("Fireball!")
    sleep(sleep_speed)
    # Fade A1L1 - 5
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
    # Fade A1L1 - 6
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
    # Fade A1L2 - 6
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
    # Fade A1L3 - 6)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 10)
    sleep(sleep_speed)
    PYGLOW.led(5, 20)
    sleep(sleep_speed)
    PYGLOW.led(6, 30)
    sleep(sleep_speed)
    # Fade A1L4 - 6)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 10)
    sleep(sleep_speed)
    PYGLOW.led(6, 20)
    sleep(sleep_speed)
    # Fade A1L5 - 6)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 10)
    sleep(sleep_speed)
    # Fade A1L6)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    # Pause before next shooting star
    sleep(0.25)


def shooting_star_2():
    ''' Turn on Arm 2 LEDS and fade '''
    LOGGER.debug("Shooting Star 2")

    sleep_speed = 0.01

    # Turn on A2L7
    PYGLOW.led(7, 60)
    sleep(sleep_speed)
    # Turn on A2L8
    PYGLOW.led(8, 60)
    sleep(sleep_speed)
    # Fade A2L7
    PYGLOW.led(7, 50)
    sleep(sleep_speed)
    # Turn on A2L9
    PYGLOW.led(9, 60)
    sleep(sleep_speed)
    # Fade A2L7 - 8
    PYGLOW.led(7, 40)
    sleep(sleep_speed)
    PYGLOW.led(8, 50)
    sleep(sleep_speed)
    # Turn on A2L10
    PYGLOW.led(10, 60)
    sleep(sleep_speed)
    # Fade A2L7 - 9
    PYGLOW.led(7, 30)
    sleep(sleep_speed)
    PYGLOW.led(8, 40)
    sleep(sleep_speed)
    PYGLOW.led(9, 50)
    sleep(sleep_speed)
    # Turn on A2L11
    PYGLOW.led(11, 60)
    sleep(sleep_speed)
    # Fade A2L7 - 10
    PYGLOW.led(7, 20)
    sleep(sleep_speed)
    PYGLOW.led(8, 30)
    sleep(sleep_speed)
    PYGLOW.led(9, 40)
    sleep(sleep_speed)
    PYGLOW.led(10, 50)
    sleep(sleep_speed)
    # Turn on A2L12
    brightness = random_brightness()
    PYGLOW.led(12, brightness)
    if brightness > 250:
        print("Fireball!")
    sleep(sleep_speed)
    # Fade A2L7 - 11
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
    # Fade A2L7 - 12
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
    # Fade A2L8 - 12
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
    # Fade A2L9 - 12
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 10)
    sleep(sleep_speed)
    PYGLOW.led(11, 20)
    sleep(sleep_speed)
    PYGLOW.led(12, 30)
    sleep(sleep_speed)
    # Fade A2L10 - 12
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 10)
    sleep(sleep_speed)
    PYGLOW.led(12, 20)
    sleep(sleep_speed)
    # Fade A2L11 - 12
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 10)
    sleep(sleep_speed)
    # Fade A2L12
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Pause before next shooting star
    sleep(0.25)


def shooting_star_3():
    ''' Turn on Arm 3 LEDS and fade '''
    LOGGER.debug("Shooting Star 3")

    sleep_speed = 0.01

    # Turn on A3L13
    PYGLOW.led(13, 60)
    sleep(sleep_speed)
    # Turn on A3L14
    PYGLOW.led(14, 60)
    sleep(sleep_speed)
    # Fade A3L13
    PYGLOW.led(13, 50)
    sleep(sleep_speed)
    # Turn on A3L15
    PYGLOW.led(15, 60)
    sleep(sleep_speed)
    # Fade A3L13 - 14
    PYGLOW.led(13, 40)
    sleep(sleep_speed)
    PYGLOW.led(14, 50)
    sleep(sleep_speed)
    # Turn on A3L16
    PYGLOW.led(16, 60)
    sleep(sleep_speed)
    # Fade A3L13 - 15
    PYGLOW.led(13, 30)
    sleep(sleep_speed)
    PYGLOW.led(14, 40)
    sleep(sleep_speed)
    PYGLOW.led(15, 50)
    sleep(sleep_speed)
    # Turn on A3L17
    PYGLOW.led(17, 60)
    sleep(sleep_speed)
    # Fade A3L13 - 16
    PYGLOW.led(13, 20)
    sleep(sleep_speed)
    PYGLOW.led(14, 30)
    sleep(sleep_speed)
    PYGLOW.led(15, 40)
    sleep(sleep_speed)
    PYGLOW.led(16, 50)
    sleep(sleep_speed)
    # Turn on A3L18
    brightness = random_brightness()
    PYGLOW.led(18, brightness)
    if brightness > 250:
        print("Fireball!")
    sleep(sleep_speed)
    # Fade A3L13 - 17
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
    # Fade A3L13 - 18
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
    # Fade A3L14 - 18
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
    # Fade A3L15 - 18
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 10)
    sleep(sleep_speed)
    PYGLOW.led(17, 20)
    sleep(sleep_speed)
    PYGLOW.led(18, 30)
    sleep(sleep_speed)
    # Fade A3L16 - 18
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 10)
    sleep(sleep_speed)
    PYGLOW.led(18, 20)
    sleep(sleep_speed)
    # Fade A3L17 - 18
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 10)
    sleep(sleep_speed)
    # Fade A3L18
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Pause before next shooting star
    sleep(0.25)


def main():
    """ The main fuction """
    LOGGER.debug("START")

    # 1, 2, and 3
    shooting_star_1()
    shooting_star_2()
    shooting_star_3()
    # 2, 3, 1
    shooting_star_2()
    shooting_star_3()
    shooting_star_1()
    # 3, 1, 2
    shooting_star_3()
    shooting_star_1()
    shooting_star_2()
    # 1, 3, 2
    shooting_star_1()
    shooting_star_3()
    shooting_star_2()
    # 3, 2, 1
    shooting_star_3()
    shooting_star_2()
    shooting_star_1()
    # 2, 1, 3
    shooting_star_2()
    shooting_star_1()
    shooting_star_3()

    LOGGER.debug("END")

    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exists.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/32_meteor_shower_with_fireballs.log'
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
