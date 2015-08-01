################################################################
#              One Through Eighteen version 2                  #
################################################################
# Description:                                                 #
# This program lights up LEDs 1 through 18 one at at time and  #
# gradually increases the speed.                               #
#                                                              #
# Version 2: The difference in this version is that instead    #
# of running countinously when the speed increases to 0.05,    # 
# it only runs 10 times, then goes back to increasing the      #
# speed. Which then runs 10 times...                           #
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

def run_10_times():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Running 10 times..."
    counter = 10
    while counter > 0:
        # Set (or Reset) led_number to 1
        led_number = 1
        ''' Uncomment the following line for feedback while the program is running '''
        #print "counter = ", counter
        while led_number < 19:
            # light up LED 
            pyglow.led(led_number,100)
            sleep(0.05)
            # turn off LED
            pyglow.led(led_number,0)
            sleep(0.05)
            # increment LED number
            led_number += 1
        # decrease counter
        counter -= 1
    increase_speed()

def increase_speed():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    led_number = 1
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        # print "The speed is now: ", sleep_speed
        while led_number < 19:
            #lightup LED 
            pyglow.led(led_number,100)
            sleep(sleep_speed)
            # turn off LED
            pyglow.led(led_number,0)
            sleep(sleep_speed)
            led_number += 1
        # Reset LED number to 1
        led_number = 1
        # Increase speed
        sleep_speed -= 0.05
    run_10_times()

increase_speed()
