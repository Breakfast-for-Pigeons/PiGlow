#!/usr/bin/env python3
"""
One Through Eighteen

This program lights up LEDs 1 through 18 one at at time and
gradually increases the speed.

....................

Functions:

- one_through_eighteen_1: Lights up LEDs one at a time
- one_through_eighteen_2: Cycles through the LEDs 10 times at max speed

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

from time import sleep
from PyGlow import PyGlow
from bfp_piglow_modules import print_header
from bfp_piglow_modules import stop

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

########################################################################
#                            Functions                                 #
########################################################################


def one_through_eighteen_1():
    """
    Lights up and turns off one LED one at a time, starting with LED 1
    and ending with LED 18. The process is done a total of 5 times, each
    time increasing the speed by 0.05.
    """

    sleep_speed = 0.25

    while sleep_speed > 0.05:

        # Start led number at 1, end at 18, increment by 1
        for i in range(1, 19, 1):
            PYGLOW.led(i, 100)       # light up LED
            sleep(sleep_speed)
            PYGLOW.led(i, 0)         # turn off LED
            sleep(sleep_speed)
        sleep_speed -= 0.05          # Increase speed


def one_through_eighteen_2():
    """
    Lights up and turns off one LED one at a time, starting with LED 1
    and ending with LED 18. Cycles through all the LEDs 10 times at a
    speed of 0.05.

    """

    # Start counter at 1, end at 10
    for _ in range(1, 10):
        # Start led number at 1, end at 18, increment by 1
        for j in range(1, 19, 1):
            PYGLOW.led(j, 100)    # light up LED
            sleep(0.05)
            PYGLOW.led(j, 0)      # turn off LED
            sleep(0.05)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03: Light up LEDs 1 through 18
        one_through_eighteen_1()
        one_through_eighteen_2()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
