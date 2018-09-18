#!/usr/bin/python3
"""
Exploding Snakes

I think the title is self explanatory. The snakes start pulsing and
eventually explode.

....................

Functions:

- explode_snake_12_or_21: Lights up and turns off the LEDs on arms 1 and 2
- explode_snake_13_or_31: Lights up and turns off the LEDs on arms 1 and 3
- explode_snake_23_or_32: Lights up and turns off the LEDs on arms 2 and 3

....................

Requirements: PyGlow.py

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
from PyGlow import PyGlow

########################################################################
#                           Variables                                  #
########################################################################

PYGLOW = PyGlow()
SLEEP_SPEED = 0.10

########################################################################
#                            Lists                                     #
########################################################################

# LEDs for snakes 12 and 21
SNAKE_12_LEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# LEDs for snakes 13 and 31
SNAKE_13_LEDS = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# LEDs for snakes 23 and 32
SNAKE_23_LEDS = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    The main function
    """
    print("Press Ctrl-C to stop the program.")
    try:
        while True:
            # 12, 13, 23
            exploding_snake_12()
            exploding_snake_13()
            exploding_snake_23()
            # 13, 23, 12
            exploding_snake_13()
            exploding_snake_23()
            exploding_snake_12()
            # 23, 12, 13
            exploding_snake_23()
            exploding_snake_12()
            exploding_snake_13()
            # 12, 23, 13
            exploding_snake_12()
            exploding_snake_23()
            exploding_snake_13()
            # 23, 13, 12
            exploding_snake_23()
            exploding_snake_13()
            exploding_snake_12()
            # 13, 12, 23
            exploding_snake_13()
            exploding_snake_12()
            exploding_snake_23()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def exploding_snake_12():
    """
    Lights up and turns off the LEDs on arms 1 and 2
    """

    explode_speed = 0.020
    pulse_speed = 175

    while pulse_speed < 225:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.led(SNAKE_12_LEDS, 100, speed=pulse_speed, pulse=True)
        sleep(0)
        pulse_speed += 1
    PYGLOW.led(SNAKE_12_LEDS, 100)
    sleep(1)
    # Explode Snake 12
    # Uncomment the following line for testing/debugging
    # print("Exploding Snake 12...")
    PYGLOW.led(6, 0)
    sleep(explode_speed)
    PYGLOW.led(18, 0)
    sleep(explode_speed)
    PYGLOW.led(11, 0)
    sleep(explode_speed)
    PYGLOW.led(5, 0)
    sleep(explode_speed)
    PYGLOW.led(10, 0)
    sleep(explode_speed)
    PYGLOW.led(4, 0)
    sleep(explode_speed)
    PYGLOW.led(9, 0)
    sleep(explode_speed)
    PYGLOW.led(3, 0)
    sleep(explode_speed)
    PYGLOW.led(8, 0)
    sleep(explode_speed)
    PYGLOW.led(2, 0)
    sleep(explode_speed)
    PYGLOW.led(7, 0)
    sleep(explode_speed)
    PYGLOW.led(1, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


def exploding_snake_13():
    """
    Lights up and turns off the LEDs on arms 1 and 3
    """

    explode_speed = 0.020
    pulse_speed = 175

    while pulse_speed < 225:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.led(SNAKE_13_LEDS, 100, speed=pulse_speed, pulse=True)
        sleep(0)
        pulse_speed += 1
    PYGLOW.led(SNAKE_13_LEDS, 100)
    sleep(1)
    # Explode Snake 13
    # Uncomment the following line for testing/debugging
    # print("Exploding Snake 13...")
    PYGLOW.led(18, 0)
    sleep(explode_speed)
    PYGLOW.led(12, 0)
    sleep(explode_speed)
    PYGLOW.led(17, 0)
    sleep(explode_speed)
    PYGLOW.led(5, 0)
    sleep(explode_speed)
    PYGLOW.led(16, 0)
    sleep(explode_speed)
    PYGLOW.led(4, 0)
    sleep(explode_speed)
    PYGLOW.led(15, 0)
    sleep(explode_speed)
    PYGLOW.led(3, 0)
    sleep(explode_speed)
    PYGLOW.led(14, 0)
    sleep(explode_speed)
    PYGLOW.led(2, 0)
    sleep(explode_speed)
    PYGLOW.led(13, 0)
    sleep(explode_speed)
    PYGLOW.led(1, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


def exploding_snake_23():
    """
    Lights up and turns off the LEDs on arms 2 and 3
    """

    explode_speed = 0.020
    pulse_speed = 175

    while pulse_speed < 225:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.led(SNAKE_23_LEDS, 100, speed=pulse_speed, pulse=True)
        sleep(0)
        pulse_speed += 1
    PYGLOW.led(SNAKE_23_LEDS, 100)
    sleep(1)
    # Uncomment the following line for testing/debugging
    # print("Exploding Snake 23...")
    # Explode Snake 13
    PYGLOW.led(6, 0)
    sleep(explode_speed)
    PYGLOW.led(12, 0)
    sleep(explode_speed)
    PYGLOW.led(11, 0)
    sleep(explode_speed)
    PYGLOW.led(17, 0)
    sleep(explode_speed)
    PYGLOW.led(10, 0)
    sleep(explode_speed)
    PYGLOW.led(16, 0)
    sleep(explode_speed)
    PYGLOW.led(9, 0)
    sleep(explode_speed)
    PYGLOW.led(15, 0)
    sleep(explode_speed)
    PYGLOW.led(8, 0)
    sleep(explode_speed)
    PYGLOW.led(14, 0)
    sleep(explode_speed)
    PYGLOW.led(7, 0)
    sleep(explode_speed)
    PYGLOW.led(13, 0)
    sleep(explode_speed)
    # Pause before next snake
    sleep(2)


if __name__ == '__main__':
    main()
