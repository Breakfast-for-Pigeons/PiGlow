################################################################
#                     One Through Eighteen                     #
################################################################
# Description:                                                 #
# This program lights up LEDs 1 through 18 one at at time and  #
# gradually increases the speed. Once the sleep_speed variable #
# decreases to 0.05, the programs runs continuously.           #
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

# Functions
def run_continuously():
    ''' Uncomment the following line if you want feedback while the program is running '''
    #print "Running continously..."
    while True:
        # Set (and Reset) led_number to 1
        led_number = 1
        while led_number < 19:
            #lightup LED 
            pyglow.led(led_number,100)
            sleep(0.05)
            # turn off LED
            pyglow.led(led_number,0)
            sleep(0.05)
            led_number += 1

def increase_speed():
    ''' Uncomment the following line if you want feedback while the program is running '''
    #print "Increasing speed..."
    led_number = 1
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line if you want feedback while the program is running '''
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
        # Pause 1 second before next loop
        sleep(sleep_speed)
    run_continuously()

# Start the program
increase_speed()
