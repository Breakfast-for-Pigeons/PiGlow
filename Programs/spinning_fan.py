#!/usr/bin/python3
"""
Spinning Fan

This program lights up the individual arms one at at time,
and  then gradually increases the speed.  Then the program
starts over again.

....................

Functions:

- spinning_fan: Turns on one arm at a time.
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
LOG = 'spinning_fan.log'
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
        spinning_fan()
        go_fast()
        go_faster()
        go_really_fast()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def spinning_fan():
    """
    Turns on one arm at a time.
    """
    LOGGER.debug("Increasing speed...")

    sleep_speed = 0.5

    while sleep_speed > 0.05:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
        # Increase speed
        sleep_speed -= 0.05


def go_fast():
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    LOGGER.debug("Going fast...")

    sleep_speed = 0.05

    while sleep_speed > 0.01:
        LOGGER.debug("The speed is now: %s", sleep_speed)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)
        # decrease counter
        sleep_speed -= 0.0025


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    LOGGER.debug("Going faster...")

    sleep_speed = 0.01

    # Start counter at 1, end at 50, increment by 1
    for i in range(1, 51, 1):
        LOGGER.debug("counter = %s", i)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)


def go_really_fast():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    LOGGER.debug("Going really fast...")

    sleep_speed = 0

    # Start counter at 1, end at 100, increment by 1
    for i in range(1, 101, 1):
        LOGGER.debug("counter = %s", i)
        # Arm 1
        PYGLOW.arm(1, 100)
        sleep(sleep_speed)
        PYGLOW.arm(1, 0)
        # Arm 2
        PYGLOW.arm(2, 100)
        sleep(sleep_speed)
        PYGLOW.arm(2, 0)
        # Arm 3
        PYGLOW.arm(3, 100)
        sleep(sleep_speed)
        PYGLOW.arm(3, 0)


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
