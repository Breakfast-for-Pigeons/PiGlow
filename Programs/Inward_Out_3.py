################################################################
#                        Inward Out 3                          #
################################################################
# Description:                                                 #
# A variation of Inward Out. This program lights up the        #
# indivdual colors like in Inward Out 2, but the lights are    #
# turned off in the same order they were turned on instead     #
# of in reverse order.Then the speeed gradually increases.     #
# Then the program starts                                      #
# over again.                                                  #
#                                                              #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

#Initialize
pyglow.all(0)

# Variables
led_brightness = 100
# sleep_speed = 0.25

# Functions
def red_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Red
    pyglow.led(13,led_brightness)
    sleep(sleep_speed)
    # Arm 2, Red
    pyglow.led(7,led_brightness)
    sleep(sleep_speed)
    # Arm 3, Red
    pyglow.led(1,led_brightness)
    sleep(sleep_speed)

def red_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Red
    pyglow.led(13,0)
    sleep(sleep_speed)
    # Arm 2, Red
    pyglow.led(7,0)
    sleep(sleep_speed)
    # Arm 3, Red
    pyglow.led(1,0)
    sleep(sleep_speed)

def orange_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Orange
    pyglow.led(14,led_brightness)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,led_brightness)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(2,led_brightness)
    sleep(sleep_speed)

def orange_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Orange
    pyglow.led(14,0)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,0)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(2,0)
    sleep(sleep_speed)

def yellow_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Yellow
    pyglow.led(15,led_brightness)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,led_brightness)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(3,led_brightness)
    sleep(sleep_speed)

def yellow_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Yellow
    pyglow.led(15,0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(3,0)
    sleep(sleep_speed)

def green_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Green
    pyglow.led(16,led_brightness)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,led_brightness)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(4,led_brightness)
    sleep(sleep_speed)

def green_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Green
    pyglow.led(16,0)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,0)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(4,0)
    sleep(sleep_speed)

def blue_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Blue
    pyglow.led(17,led_brightness)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,led_brightness)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(5,led_brightness)
    sleep(sleep_speed)

def blue_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Blue
    pyglow.led(17,0)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,0)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(5,0)
    sleep(sleep_speed)

def white_leds_on(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, White
    pyglow.led(18,led_brightness)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,led_brightness)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(6,led_brightness)
    sleep(sleep_speed)

def white_leds_off(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, White
    pyglow.led(18,0)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,0)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(6,0)
    sleep(sleep_speed)

def increase_speed():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        # print "The speed is now: ", sleep_speed
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    go_fast(sleep_speed)

def go_fast(sleep_speed):
    sleep_speed = 0.05
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going fast..."
    while sleep_speed > 0.01:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "counter = ", counter
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # decrease counter
        sleep_speed -= 0.0025
    go_faster()

def go_faster():
    sleep_speed = 0.01
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going faster..."
    counter = 20
    while counter > 0:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "counter = ", counter
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # decrease counter
        counter -= 1
    go_really_fast()

def go_really_fast():
    sleep_speed = 0
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going really fast..."
    counter = 100
    while counter > 0:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "counter = ", counter
        # Turn on LEDs
        white_leds_on(sleep_speed)
        blue_leds_on(sleep_speed)
        green_leds_on(sleep_speed)
        yellow_leds_on(sleep_speed)
        orange_leds_on(sleep_speed)
        red_leds_on(sleep_speed)
        # Turn off LEDs
        white_leds_off(sleep_speed)
        blue_leds_off(sleep_speed)
        green_leds_off(sleep_speed)
        yellow_leds_off(sleep_speed)
        orange_leds_off(sleep_speed)
        red_leds_off(sleep_speed)
        # decrease counter
        # decrease counter
        counter -= 1
    increase_speed()

# Start the Program
increase_speed()
