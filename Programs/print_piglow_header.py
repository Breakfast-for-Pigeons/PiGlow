#!/usr/bin/python3
"""
Print PiGlow Header

This is the print_piglow_header module for my PiGlow programs.

....................

Functions:

- print_pyglow_header: Prints a header

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
import logging

# Logging
LOG = 'Logs/print_piglow_header.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)    # Nothing will log unless changed to DEBUG
FORMATTER = logging.Formatter(fmt=LOG_FORMAT,
                              datefmt='%m/%d/%y %I:%M:%S %p:')
FILE_HANDLER = logging.FileHandler(LOG, 'w')
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)

def print_piglow_header():
    """
    Prints a header


    This function will print out the program header ina randomly
    selected color.
    """

    LOGGER.debug("Printing PiGlow header...")

    import random

    color_list = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                  '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                  '\033[1;37;40m']

    color = random.choice(color_list)

    print(color)
    print(r"""


        ***** **                  * ***      ***
     ******  ****     *         *  ****  *    ***
    **   *  *  ***   ***       *  *  ****      **               **
   *    *  *    ***   *       *  **   **       **               **
       *  *      **          *  ***            **       ****     **    ***    ****
      ** **      ** ***     **   **            **      * ***  *   **    ***     ***  *
      ** **      **  ***    **   **   ***      **     *   ****    **     ***     ****
    **** **      *    **    **   **  ****  *   **    **    **     **      **      **
   * *** **     *     **    **   ** *  ****    **    **    **     **      **      **
      ** *******      **    **   ***    **     **    **    **     **      **      **
      ** ******       **     **  **     *      **    **    **     **      **      **
      ** **           **      ** *      *      **    **    **     **      **      *
      ** **           **       ***     *       **     ******       ******* *******
      ** **           *** *     *******        *** *   ****         *****   *****
 **   ** **            ***        ***           ***
***   *  *
 ***    *
  ******
    ***


    """)


if __name__ == '__main__':
    print_piglow_header()
