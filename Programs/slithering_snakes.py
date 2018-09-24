#!/usr/bin/python3
"""
Slithering Snakes

I think the title is self explanatory.

....................

Functions:
- slithering_snake_12: Lights up then turns off the LEDs on arms 1 and 2
- slithering_snake_13: Lights up then turns off the LEDs on arms 1 and 3
- slithering_snake_21: Lights up then turns off the LEDs on arms 2 and 1
- slithering_snake_23: Lights up then turns off the LEDs on arms 2 and 3
- slithering_snake_31: Lights up then turns off the LEDs on arms 3 and 1
- slithering_snake_32: Lights up then turns off the LEDs on arms 3 and 2
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
LOG = 'slithering_snakes.log'
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
        # Snakes 12, 13, 21, 23, 31, 32
        slithering_snake_12()
        slithering_snake_13()
        slithering_snake_21()
        slithering_snake_23()
        slithering_snake_31()
        slithering_snake_32()
        # Snakes 12, 23, 31, 13, 32, 21
        slithering_snake_12()
        slithering_snake_23()
        slithering_snake_31()
        slithering_snake_13()
        slithering_snake_32()
        slithering_snake_21()
        # Snakes 13, 12, 23, 21, 31, 32
        slithering_snake_13()
        slithering_snake_12()
        slithering_snake_23()
        slithering_snake_21()
        slithering_snake_31()
        slithering_snake_32()
        # Snakes 13, 32, 21, 12, 23, 31
        slithering_snake_13()
        slithering_snake_32()
        slithering_snake_21()
        slithering_snake_12()
        slithering_snake_23()
        slithering_snake_31()
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def slithering_snake_12():
    """
    Lights up then turns off the LEDs on arms 1 and 2
    """
    LOGGER.debug("Slithering Snake 1-2")

    sleep_speed = 0.10

    # Light up Snake 12
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    # Turn off Snake 12
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Pause before next snake
    sleep(1)


def slithering_snake_13():
    """
    Lights up then turns off the LEDs on arms 1 and 3
    """
    LOGGER.debug("Slithering Snake 1-3")

    sleep_speed = 0.10

    # Light up Snake 13
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Turn off Snake 13
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Pause before next snake
    sleep(1)


def slithering_snake_21():
    """
    Lights up then turns off the LEDs on arms 2 and 1
    """
    LOGGER.debug("Slithering Snake 2-1")

    sleep_speed = 0.10

    # Light up Snake 21
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    # Turn off Snake 21
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    # Pause before next snake
    sleep(1)


def slithering_snake_23():
    """
    Lights up then turns off the LEDs on arms 2 and 3
    """
    LOGGER.debug("Slithering Snake 2-3")

    sleep_speed = 0.10

    # Light up Snake 23
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    # Turn off Snake 23
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Pause before next snake
    sleep(1)


def slithering_snake_31():
    """
    Lights up then turns off the LEDs on arms 3 and 1
    """
    LOGGER.debug("Slithering Snake 3-1")

    sleep_speed = 0.10

    # Light up Snake 31
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(18, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(5, 100)
    sleep(sleep_speed)
    PYGLOW.led(4, 100)
    sleep(sleep_speed)
    PYGLOW.led(3, 100)
    sleep(sleep_speed)
    PYGLOW.led(2, 100)
    sleep(sleep_speed)
    PYGLOW.led(1, 100)
    sleep(sleep_speed)
    # Turn off Snake 31
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)
    PYGLOW.led(2, 0)
    sleep(sleep_speed)
    PYGLOW.led(1, 0)
    sleep(sleep_speed)
    # Pause before next snake
    sleep(1)


def slithering_snake_32():
    """
    Lights up then turns off the LEDs on arms 3 and 2
    """
    LOGGER.debug("Slithering Snake 3-2")

    sleep_speed = 0.10

    # Light up Snake 32
    PYGLOW.led(13, 100)
    sleep(sleep_speed)
    PYGLOW.led(14, 100)
    sleep(sleep_speed)
    PYGLOW.led(15, 100)
    sleep(sleep_speed)
    PYGLOW.led(16, 100)
    sleep(sleep_speed)
    PYGLOW.led(17, 100)
    sleep(sleep_speed)
    PYGLOW.led(6, 100)
    sleep(sleep_speed)
    PYGLOW.led(12, 100)
    sleep(sleep_speed)
    PYGLOW.led(11, 100)
    sleep(sleep_speed)
    PYGLOW.led(10, 100)
    sleep(sleep_speed)
    PYGLOW.led(9, 100)
    sleep(sleep_speed)
    PYGLOW.led(8, 100)
    sleep(sleep_speed)
    PYGLOW.led(7, 100)
    sleep(sleep_speed)
    # Turn off Snake 32
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Pause before next snake
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
