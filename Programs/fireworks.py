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
LOG = 'fireworks.log'
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
            LOGGER.debug("Fireworks #%s", counter)
            fireworks()
            counter += 1
        stop()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def fireworks():
    """
    Lights up 1 color at a time, Fades colors
    """

    sleep_speed = 0.025

    # Turn on white
    PYGLOW.color("white", 60)
    sleep(sleep_speed)
    # Turn on blue
    PYGLOW.color("blue", 60)
    sleep(sleep_speed)
    # Fade white
    PYGLOW.color("white", 50)
    sleep(sleep_speed)
    # Turn on green
    PYGLOW.color("green", 60)
    sleep(sleep_speed)
    # Fade white and blue
    PYGLOW.color("white", 40)
    sleep(sleep_speed)
    PYGLOW.color("blue", 50)
    sleep(sleep_speed)
    # Turn on yellow
    PYGLOW.color("yellow", 60)
    sleep(sleep_speed)
    # Fade white, blue, and green
    PYGLOW.color("white", 30)
    sleep(sleep_speed)
    PYGLOW.color("blue", 40)
    sleep(sleep_speed)
    PYGLOW.color("green", 50)
    sleep(sleep_speed)
    # Turn on orange
    PYGLOW.color("orange", 60)
    sleep(sleep_speed)
    # Fade white, blue, green, and yellow
    PYGLOW.color("white", 20)
    sleep(sleep_speed)
    PYGLOW.color("blue", 30)
    sleep(sleep_speed)
    PYGLOW.color("green", 40)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 50)
    sleep(sleep_speed)
    # Turn on red
    PYGLOW.color("red", 60)
    sleep(sleep_speed)
    # Fade white, blue, green, yellow, and orange
    PYGLOW.color("white", 10)
    sleep(sleep_speed)
    PYGLOW.color("blue", 20)
    sleep(sleep_speed)
    PYGLOW.color("green", 30)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 40)
    sleep(sleep_speed)
    PYGLOW.color("orange", 50)
    sleep(sleep_speed)
    # Fade all
    PYGLOW.color("white", 0)
    sleep(sleep_speed)
    PYGLOW.color("blue", 10)
    sleep(sleep_speed)
    PYGLOW.color("green", 20)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 30)
    sleep(sleep_speed)
    PYGLOW.color("orange", 40)
    sleep(sleep_speed)
    PYGLOW.color("red", 50)
    sleep(sleep_speed)
    # Fade blue, green, yellow, orange, and red
    PYGLOW.color("blue", 0)
    sleep(sleep_speed)
    PYGLOW.color("green", 10)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 20)
    sleep(sleep_speed)
    PYGLOW.color("orange", 30)
    sleep(sleep_speed)
    PYGLOW.color("red", 40)
    sleep(sleep_speed)
    # Fade green, yellow, orange, and red
    PYGLOW.color("green", 0)
    sleep(sleep_speed)
    PYGLOW.color("yellow", 10)
    sleep(sleep_speed)
    PYGLOW.color("orange", 20)
    sleep(sleep_speed)
    PYGLOW.color("red", 30)
    sleep(sleep_speed)
    # Fade yellow, orange, and red
    PYGLOW.color("yellow", 0)
    sleep(sleep_speed)
    PYGLOW.color("orange", 10)
    sleep(sleep_speed)
    PYGLOW.color("red", 20)
    sleep(sleep_speed)
    # Fade orange, and red
    PYGLOW.color("orange", 0)
    sleep(sleep_speed)
    PYGLOW.color("red", 10)
    sleep(sleep_speed)
    # Fade red
    PYGLOW.color("red", 0)
    sleep(sleep_speed)
    # Pause 1 second before the next one
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
