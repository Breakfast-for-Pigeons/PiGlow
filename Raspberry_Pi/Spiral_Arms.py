################################################################
#                        Spiral Arms                           #
################################################################
# Description:                                                 #
# This program lights up the LEDs on arm 1 one at at time,     #
# then arm 2, then arm 3. Then turns off the lights one at a   #
# time. Then increases the speed and goes through the entire   #
# process again.                                               #
#                                                              #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

# Initialize
pyglow.all(0)

# Variables
''' Feel free to modify the brightness setting below '''
led_brightness = 100

# Functions
def turn_on_leds(sleep_speed):
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "Turning on LEDs..."
    # Set (or Reset) LED number
    led_number = 1
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "The current sleep speed (turn on LEDs) is:", sleep_speed
    # Turn on LEDs one at a time
    while led_number < 19:
        pyglow.led(led_number,led_brightness)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)
    
def turn_off_leds(sleep_speed):
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "Turning off LEDs..."
    # Set (or Reset) LED number
    led_number = 1
    # Turn on LEDs one at a time
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "The current sleep speed (turn off LEDs) is:", sleep_speed
    while led_number < 19:
        pyglow.led(led_number,0)
        sleep(sleep_speed)
        led_number += 1
    sleep(sleep_speed)
    
def increase_speed():
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following print statement for feedback while the program is running '''
        #print "The current speed is:", sleep_speed
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    run_10_times()  
    
def run_10_times():
    ''' Uncomment the following print statement for feedback while the program is running '''
    #print "Running 10 times..."
    # Set counter to 5
    counter = 10
    # Reset led_number to 1
    led_number = 1
    # Set sleep_speed to 0.05
    sleep_speed = 0.05
    while counter > 0:
        ''' Uncomment the following print statement for feedback while the program is running '''
        #print "Running number:", counter
        turn_on_leds(sleep_speed)
        turn_off_leds(sleep_speed)
        # Decrease counter
        counter -= 1
    increase_speed()

# Start the program
try:   
    increase_speed()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
