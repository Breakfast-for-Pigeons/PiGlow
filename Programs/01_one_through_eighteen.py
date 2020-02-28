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


def one_through_eighteen_1():
    """
    Lights up and turns off one LED one at a time, starting with LED 1
    and ending with LED 18. The process is done a total of 5 times, each
    time increasing the speed by 0.05.
    """
    LOGGER.debug("Function: one_through_eighteen_1")
    LOGGER.debug("Lighting up LEDs 1 through 18...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now %s", sleep_speed)
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
    LOGGER.debug("Function: one_through_eighteen_2")
    LOGGER.debug("Running 10 times...")

    # Start counter at 1, end at 10, increment by 1
    for i in range(1, 11, 1):
        LOGGER.debug("counter is: %s", i)
        # Start led number at 1, end at 18, increment by 1
        for j in range(1, 19, 1):
            PYGLOW.led(j, 100)    # light up LED
            sleep(0.05)
            PYGLOW.led(j, 0)      # turn off LED
            sleep(0.05)


def main():
    """
    This is the main function.
    """
    LOGGER.debug("START")
    one_through_eighteen_1()
    one_through_eighteen_2()
    LOGGER.debug("END")
    delete_empty_logs(LOG)
    stop()


if __name__ == '__main__':
    try:
        # STEP01: Check if Log directory exits.
        check_log_directory()
        # STEP02: Enable logging
        LOG = 'Logs/01_one_through_eighteen.log'
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
