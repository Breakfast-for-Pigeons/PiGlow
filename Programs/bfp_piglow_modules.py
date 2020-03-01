#!/usr/bin/python3
"""
bfp_piglow,py

This is a module containing the support functions and variables for my
piGlow programs. Each program imports only the needed functions and
variables.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import os
import random
from PyGlow import PyGlow

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

########################################################################
#                           Variables                                  #
########################################################################

HEADER_COLORS = ['\033[1;31;40m', '\033[1;32;40m', '\033[1;33;40m',
                 '\033[1;34;40m', '\033[1;35;40m', '\033[1;36;40m',
                 '\033[1;37;40m']

########################################################################
#                            Functions                                 #
########################################################################


def print_header():
    """
    Prints a header


    This function will print out the program header in a randomly
    selected color.
    """

    color = random.choice(HEADER_COLORS)

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


def check_log_directory():
    """
    This functions checks to see if the log directory exits. If it
    doesn't, then it is created.
    """
    log_directory = "Logs"
    current_directory = os.getcwd()
    path_to_log = "{}/{}".format(current_directory, log_directory)

    if os.path.isdir(path_to_log):
        return
    else:
        os.mkdir(log_directory)

def delete_empty_logs(log):
    """
    Delete empty log fles

    Log files will always be created. But they will be empty if the
    log level is set to anything higher than DEBUG, since only DEBUG
    messages are logged. If the log files are empty, they will be
    deleted.
    """

    if os.stat(log).st_size == 0:
        os.remove(log)


def stop():
    """
    Print exit message and turn off the PiGlow
    """
    print("\nExiting program.")
    PYGLOW.all(0)
