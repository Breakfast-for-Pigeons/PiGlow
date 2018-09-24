#!/usr/bin/python3
"""
Swirling Vortex

This program lights up the LEDs one at a time then
then fades them on all 3 arms at the same time.

....................

Functions:
- swirling_vortex: Lights up 1 color at a time, Fades colors
- delete_empty_logs: Deletes empty log fles
- stop: Print exit message and turn off the PiGlow

....................

Requirements:
    PyGlow.py (many thanks to benleb for this program)
    print_piglow_header.py

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
LOG = 'swirling_vortex.log'
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

    counter = 1

    try:
        while counter < 11:
            LOGGER.debug("Swirling Vortex #%s", counter)
            swirling_vortex()
            sleep(1)
            counter += 1
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def swirling_vortex():
    """
    Lights up 1 color at a time, Fades colors
    """

    sleep_speed = 0.01

    # Turn on red
    PYGLOW.color("red", 60)
    sleep(sleep_speed)
    # Turn on orange
    PYGLOW.color("orange", 60)
    sleep(sleep_speed)
    # Fade red
    PYGLOW.color("red", 50)
    sleep(sleep_speed)
    # Turn on yellow
    PYGLOW.color("yellow", 60)
    sleep(sleep_speed)
    # Fade red and orange
    PYGLOW.color("red", 40)
    sleep(sleep_speed)
    PYGLOW.color("orange", 50)
    sleep(sleep_speed)
    # Turn on green
    PYGLOW.color("green", 60)
    sleep(sleep_speed)
    # Fade red, orange, and yellow
    PYGLOW.color("red", 30)
    sleep(sleep_speed)
    PYGLOW.color("orange", 40)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 50)
    sleep(sleep_speed)
    # Turn on blue
    PYGLOW.color("blue", 60)
    sleep(sleep_speed)
    # Fade red, orange, yellow, green
    PYGLOW.color("red", 20)
    sleep(sleep_speed)
    PYGLOW.color("orange", 30)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 40)
    sleep(sleep_speed)
    PYGLOW.color("green", 50)
    sleep(sleep_speed)
    # Turn on white
    PYGLOW.color("white", 60)
    sleep(sleep_speed)
    # Fade red, orange, yellow, green, and blue
    PYGLOW.color("red", 10)
    sleep(sleep_speed)
    PYGLOW.color("orange", 20)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 30)
    sleep(sleep_speed)
    PYGLOW.color("green", 40)
    sleep(sleep_speed)
    PYGLOW.color("blue", 50)
    sleep(sleep_speed)
    # Fade all
    PYGLOW.color("red", 0)
    sleep(sleep_speed)
    PYGLOW.color("orange", 10)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 20)
    sleep(sleep_speed)
    PYGLOW.color("green", 30)
    sleep(sleep_speed)
    PYGLOW.color("blue", 40)
    sleep(sleep_speed)
    PYGLOW.color("white", 50)
    sleep(sleep_speed)
    # Fade orange, yellow, green, blue, and white
    PYGLOW.color("orange", 0)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 10)
    sleep(sleep_speed)
    PYGLOW.color("green", 20)
    sleep(sleep_speed)
    PYGLOW.color("blue", 30)
    sleep(sleep_speed)
    PYGLOW.color("white", 40)
    sleep(sleep_speed)
    # Fade yellow, green, blue, and white
    PYGLOW.color("yellow", 0)
    sleep(sleep_speed)
    PYGLOW.color("green", 10)
    sleep(sleep_speed)
    PYGLOW.color("blue", 20)
    sleep(sleep_speed)
    PYGLOW.color("white", 30)
    sleep(sleep_speed)
    # Fade green, blue, and white
    PYGLOW.color("green", 0)
    sleep(sleep_speed)
    PYGLOW.color("blue", 10)
    sleep(sleep_speed)
    PYGLOW.color("white", 20)
    sleep(sleep_speed)
    # Fade blue, and white
    PYGLOW.color("blue", 0)
    sleep(sleep_speed)
    PYGLOW.color("white", 10)
    sleep(sleep_speed)
    # Fade white
    PYGLOW.color("white", 0)
    sleep(sleep_speed)


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
