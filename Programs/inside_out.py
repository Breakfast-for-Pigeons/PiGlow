#!/usr/bin/python3
"""
Inside Out

This program lights up the individual colors one at at time,
starting with the inside white leds and moving out to the
outside red. It gradually increases the speed and then goes
through the entire process again. It's Spiral Colors with
the order of the LEDs reversed.

....................

Functions:
- sprial_colors: Lights up 1 color at a time
- red_leds: Lights up the red LEDs one at a time
- orange_leds: Lights up the orange LEDs one at a time
- yellow_leds: Lights up the yellow LEDs one at a time
- green_leds: Lights up the green LEDs one at a time
- blue_leds: Lights up the blue LEDs one at a time
- white_leds: :ights up the  white LEDs one at a time
- go_fast: Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
- go_faster: Sleep_speed  is 0.01. Cycle through the LEDS 20 times
- go_really_fast: Sleep_speed is 0. Cycle through the LEDS 100 times

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

# Feel free to modify the brightness setting below
LED_BRIGHTNESS = 100

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW.all(0)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """
    The main function
    """
    print("Press Ctrl-C to stop the program.")
    try:
        inside_out()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        print("\nExiting program.")
        PYGLOW.all(0)


def red_leds(sleep_speed):
    """
    Lights up the red LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, Red
    PYGLOW.led(13, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(13, 0)
    sleep(sleep_speed)
    # Arm 2, Red
    PYGLOW.led(7, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(7, 0)
    sleep(sleep_speed)
    # Arm 1, Red
    PYGLOW.led(1, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(1, 0)
    sleep(sleep_speed)


def orange_leds(sleep_speed):
    """
    Lights up the orange LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, Orange
    PYGLOW.led(14, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(14, 0)
    sleep(sleep_speed)
    # Arm 2, Orange
    PYGLOW.led(8, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(8, 0)
    sleep(sleep_speed)
    # Arm 1, Orange
    PYGLOW.led(2, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(2, 0)
    sleep(sleep_speed)


def yellow_leds(sleep_speed):
    """
    Lights up the yellow LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, Yellow
    PYGLOW.led(15, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(15, 0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    PYGLOW.led(9, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(9, 0)
    sleep(sleep_speed)
    # Arm 1, Yellow
    PYGLOW.led(3, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(3, 0)
    sleep(sleep_speed)


def green_leds(sleep_speed):
    """
    Lights up the green LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, Green
    PYGLOW.led(16, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(16, 0)
    sleep(sleep_speed)
    # Arm 2, Green
    PYGLOW.led(10, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(10, 0)
    sleep(sleep_speed)
    # Arm 1, Green
    PYGLOW.led(4, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(4, 0)
    sleep(sleep_speed)


def blue_leds(sleep_speed):
    """
    Lights up the blue LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, Blue
    PYGLOW.led(17, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(17, 0)
    sleep(sleep_speed)
    # Arm 2, Blue
    PYGLOW.led(11, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(11, 0)
    sleep(sleep_speed)
    # Arm 1, Blue
    PYGLOW.led(5, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(5, 0)
    sleep(sleep_speed)


def white_leds(sleep_speed):
    """
    Lights up the white LEDs one at a time
    """
    sleep_speed = sleep_speed
    # Arm 3, White
    PYGLOW.led(18, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(18, 0)
    sleep(sleep_speed)
    # Arm 2, White
    PYGLOW.led(12, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(12, 0)
    sleep(sleep_speed)
    # Arm 1, White
    PYGLOW.led(6, LED_BRIGHTNESS)
    sleep(sleep_speed)
    PYGLOW.led(6, 0)
    sleep(sleep_speed)


def inside_out():
    """
    Lights up 1 color at a time

    Speed goes from 0.25 to 0.05 in decrements of 0.05
    """
    # Uncomment the following line for testing/debugging
    # print("Increasing speed...")
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        # Uncomment the following line for testing/debugging
        # print("The speed is now: ", sleep_speed)
        white_leds(sleep_speed)
        blue_leds(sleep_speed)
        green_leds(sleep_speed)
        yellow_leds(sleep_speed)
        orange_leds(sleep_speed)
        red_leds(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    go_fast(sleep_speed)


def go_fast(sleep_speed):
    """
    Sleep_speed goes from 0.05 to 0.01 in decrements of 0.0025
    """
    sleep_speed = 0.05
    # Uncomment the following line for testing/debugging
    # print("Going fast...")
    while sleep_speed > 0.01:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        white_leds(sleep_speed)
        blue_leds(sleep_speed)
        green_leds(sleep_speed)
        yellow_leds(sleep_speed)
        orange_leds(sleep_speed)
        red_leds(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025
    go_faster()


def go_faster():
    """
    Sleep_speed is 0.01. Cycle through the LEDS 20 times
    """
    sleep_speed = 0.01
    # Uncomment the following line for testing/debugging
    # print("Going faster...")
    counter = 20
    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        white_leds(sleep_speed)
        blue_leds(sleep_speed)
        green_leds(sleep_speed)
        yellow_leds(sleep_speed)
        orange_leds(sleep_speed)
        red_leds(sleep_speed)
        # decrease counter
        counter -= 1
    go_really_fast()


def go_really_fast():
    """
    Sleep_speed is 0. Cycle through the LEDS 100 times
    """
    sleep_speed = 0
    # Uncomment the following line for testing/debugging
    # print("Going really fast...")
    counter = 100
    while counter > 0:
        # Uncomment the following line for testing/debugging
        # print("counter = ", counter)
        white_leds(sleep_speed)
        blue_leds(sleep_speed)
        green_leds(sleep_speed)
        yellow_leds(sleep_speed)
        orange_leds(sleep_speed)
        red_leds(sleep_speed)
        # decrease counter
        counter -= 1
    inside_out()


if __name__ == '__main__':
    main()
