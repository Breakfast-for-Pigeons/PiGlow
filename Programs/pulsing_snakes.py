#!/usr/bin/python3
"""
Pulsing Snakes

I think the title is self explanatory.

....................

Functions:
- pulsing_snake_12: Lights up and pulses the LEDs on arms 1 and 2
- pulsing_snake_13: Lights up and pulses the LEDs on arms 1 and 3
- pulsing_snake_23: Lights up and pulses the LEDs on arms 2 and 3

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
SLEEP_SPEED = 1

########################################################################
#                            Lists                                     #
########################################################################

# Snake 12 LEDs (Same lights as Snake 21 - Since they are not slithering,
# the order doesn't matter)
SNAKE_12_LEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# Snake 13 LEDs (Same lights as Snake 31 - Since they are not slithering,
# the order doesn't matter)
SNAKE_13_LEDS = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# Snake 23 LEDs (Same lights as Snake 32 - Since they are not slithering,
# the order doesn't matter)
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
            pulsing_snake_12()
            pulsing_snake_13()
            pulsing_snake_23()
            # 13, 23, 12
            pulsing_snake_13()
            pulsing_snake_23()
            pulsing_snake_12()
            # 23, 12, 13
            pulsing_snake_23()
            pulsing_snake_12()
            pulsing_snake_13()
            # 12, 23, 13
            pulsing_snake_12()
            pulsing_snake_23()
            pulsing_snake_13()
            # 23, 13, 12
            pulsing_snake_23()
            pulsing_snake_13()
            pulsing_snake_12()
            # 13, 12, 23
            pulsing_snake_13()
            pulsing_snake_12()
            pulsing_snake_23()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def pulsing_snake_12():
    """
    Lights up and pulses the LEDs on arms 1 and 2
    """
    pulse_speed = 200
    while pulse_speed > 100:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.set_leds(SNAKE_12_LEDS, 100, speed=pulse_speed,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
        pulse_speed -= 1
    PYGLOW.set_leds(SNAKE_12_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


def pulsing_snake_13():
    """
    Lights up and pulses the LEDs on arms 1 and 3
    """
    pulse_speed = 200
    while pulse_speed > 100:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.set_leds(SNAKE_13_LEDS, 100, speed=pulse_speed,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
        pulse_speed -= 1
    PYGLOW.set_leds(SNAKE_13_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


def pulsing_snake_23():
    """
    Lights up and pulses the LEDs on arms 2 and 3
    """
    pulse_speed = 200
    while pulse_speed > 100:
        # Uncomment the following line for testing/debugging
        # print("Pulse speed is: ", pulse_speed)
        PYGLOW.set_leds(SNAKE_23_LEDS, 100, speed=pulse_speed,
                        pulse=True)
        sleep(0)
        PYGLOW.update_leds()
        pulse_speed -= 1
    PYGLOW.set_leds(SNAKE_23_LEDS, 0)
    PYGLOW.update_leds()
    sleep(SLEEP_SPEED)


if __name__ == '__main__':
    main()
