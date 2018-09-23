#!/usr/bin/python3
"""
One Through Eighteen

This program lights up LEDs 1 through 18 one at at time and
gradually increases the speed.

....................

Functions:

- one_through_eighteen: Lights up LEDs one at a time
- run_10_times: Cycles throught the LEDs 10 times
- stop: Print exit message and turn off the PiGlow

....................

Requirements:
    PyGlow.py
    print_pyglow_header.py
(You will have these files if you downloaded the entire repository)

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
LOG = 'Logs/01_one_through_eighteen.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)    # Nothing will log unless changed to DEBUG
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
    print("\033[1;37;40mPress Ctrl-C to stop the program.")
    try:
        one_through_eighteen()
        run_10_times()
        stop()
    except KeyboardInterrupt:
        stop()


def one_through_eighteen():
    """
    Lights up and turns off LEDs 1 through 18 one at a time.
    Gradually increases the speed at which the LEDs light up
    """

    LOGGER.debug("Increasing speed...")

    led_number = 1
    sleep_speed = 0.25

    while sleep_speed > 0.05:

        LOGGER.debug("The speed is now %s", sleep_speed)

        while led_number < 19:
            PYGLOW.led(led_number, 100)    # light up LED
            sleep(sleep_speed)
            PYGLOW.led(led_number, 0)      # turn off LED
            sleep(sleep_speed)
            led_number += 1
        led_number = 1                     # Reset LED number to 1
        sleep_speed -= 0.05                # Increase speed


def run_10_times():
    """ Run 10 times

    Once the program has reached the max set speed, it will cycle
    throught the LEDs 10 times.

    """

    LOGGER.debug("Running 10 times...")

    counter = 10

    while counter > 0:
        # Set (or Reset) led_number to 1
        led_number = 1

        LOGGER.debug("This is run number %s", counter)

        while led_number < 19:
            PYGLOW.led(led_number, 100)    # light up LED
            sleep(0.05)
            PYGLOW.led(led_number, 0)      # turn off LED
            sleep(0.05)
            led_number += 1                # increment LED number
        counter -= 1                       # decrease counter


def delete_empty_logs():
    """
    Delete empty log fles

    Log files will always be created. But they will be empty if the
    log level is set to anything higher than DEBUG, since only DEBUG
    messages are logged. If the log files are empty, they will be
    deleted.
    """

    logs = [LOG, 'Logs/print_piglow_header.log']

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
