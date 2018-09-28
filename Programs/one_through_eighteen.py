#!/usr/bin/python3
"""
One Through Eighteen

This program lights up LEDs 1 through 18 one at at time and
gradually increases the speed.

....................

Functions:

- one_through_eighteen: Lights up LEDs one at a time
- run_10_times: Cycles throught the LEDs 10 times
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
LOG = 'one_through_eighteen.log'
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
        increase_speed()
        run_10_times()
        stop()
    except KeyboardInterrupt:
        stop()


def increase_speed():
    """
    Lights up and turns off LEDs 1 through 18 one at a time.
    Gradually increases the speed at which the LEDs light up
    """
    LOGGER.debug("Lighting up LEDs 1 through 18...")

    sleep_speed = 0.25

    while sleep_speed > 0.05:

        LOGGER.debug("The speed is now %s", sleep_speed)

        # Start led number at 1, end at 18, increment by 1
        for i in range(1, 19, 1):
            PYGLOW.led(i, 100)    # light up LED
            sleep(sleep_speed)
            PYGLOW.led(i, 0)      # turn off LED
            sleep(sleep_speed)
        sleep_speed -= 0.05                # Increase speed


def run_10_times():
    """ Run 10 times

    Cycles through all the LEDs 10 times at a speed of 0.05.

    """
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
