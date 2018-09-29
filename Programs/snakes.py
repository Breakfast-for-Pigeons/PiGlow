#!/usr/bin/python3
"""
Snakes (or should the title be: Pythons)

I think the title is self explanatory.

....................

Functions:
- snake_12: Lights up the LEDs on arms 1 and 2
- snake_13: Lights up the LEDs on arms 1 and 3
- snake_23: Lights up the LEDs on arms 2 and 3
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
LOG = 'snakes.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)    # Nothing will log unless changed to DEBUG
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
        # Start counter at 1, end at 3, increment by 1
        for i in range(1, 4, 1):
            LOGGER.debug("counter = %s", i)
            snake_12()
            snake_23()
            snake_13()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()

def snake_12():
    """
    Lights up the LEDs on arms 1 and 2
    """
    LOGGER.debug("Lighting up Snake 1-2")

    # Snake 12 LEDs (Same lights as Snake 21 - Since they are not
    # slithering, the order doesn't matter)
    snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
    sleep_speed = 2

    PYGLOW.set_leds(snake_12_leds, 100)
    PYGLOW.update_leds()
    sleep(sleep_speed)
    PYGLOW.set_leds(snake_12_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


def snake_13():
    """
    Lights up the LEDs on arms 1 and 3
    """
    LOGGER.debug("Lighting up Snake 1-3")

    # Snake 13 LEDs (Same lights as Snake 31 - Since they are not
    # slithering, the order doesn't matter)
    snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
    sleep_speed = 2

    PYGLOW.set_leds(snake_13_leds, 100)
    PYGLOW.update_leds()
    sleep(sleep_speed)
    PYGLOW.set_leds(snake_13_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


def snake_23():
    """
    Lights up the LEDs on arms 2 and 3
    """
    LOGGER.debug("Lighting up Snake 2-3")

    # Snake 23 LEDs (Same lights as Snake 32 - Since they are not
    # slithering, the order doesn't matter)
    snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    sleep_speed = 2

    PYGLOW.set_leds(snake_23_leds, 100)
    PYGLOW.update_leds()
    sleep(sleep_speed)
    PYGLOW.set_leds(snake_23_leds, 0)
    PYGLOW.update_leds()
    sleep(1)


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
