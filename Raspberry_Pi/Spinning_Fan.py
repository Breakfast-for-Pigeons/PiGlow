################################################################
#                        Spinning Fan                          #
################################################################
# Description:                                                 #
# This program lights up the individual arms one at at time,   #
# and  then gradually increases the speed.  Then the program   #
# starts over again.                                           #
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
# sleep_speed = 1


def spinning_fan():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.5
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        # print "The speed is now: ", sleep_speed
        # Arm 1
        pyglow.arm(1, 100)
        sleep(sleep_speed)
        pyglow.arm(1, 0)
        # Arm 2
        pyglow.arm(2, 100)
        sleep(sleep_speed)
        pyglow.arm(2, 0)
        # Arm 3
        pyglow.arm(3, 100)
        sleep(sleep_speed)
        pyglow.arm(3, 0)
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
        # Arm 1
        pyglow.arm(1, 100)
        sleep(sleep_speed)
        pyglow.arm(1, 0)
        # Arm 2
        pyglow.arm(2, 100)
        sleep(sleep_speed)
        pyglow.arm(2, 0)
        # Arm 3
        pyglow.arm(3, 100)
        sleep(sleep_speed)
        pyglow.arm(3, 0)
        # decrease counter
        sleep_speed -= 0.0025
    go_faster()

def go_faster():
    sleep_speed = 0.01
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going faster..."
    counter = 50
    while counter > 0:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "counter = ", counter
        # Arm 1
        pyglow.arm(1, 100)
        sleep(sleep_speed)
        pyglow.arm(1, 0)
        # Arm 2
        pyglow.arm(2, 100)
        sleep(sleep_speed)
        pyglow.arm(2, 0)
        # Arm 3
        pyglow.arm(3, 100)
        sleep(sleep_speed)
        pyglow.arm(3, 0)
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
        # Arm 1
        pyglow.arm(1, 100)
        sleep(sleep_speed)
        pyglow.arm(1, 0)
        # Arm 2
        pyglow.arm(2, 100)
        sleep(sleep_speed)
        pyglow.arm(2, 0)
        # Arm 3
        pyglow.arm(3, 100)
        sleep(sleep_speed)
        pyglow.arm(3, 0)
        # decrease counter
        counter -= 1
    sleep(2)
    spinning_fan()

# Start the Program
try:  
    spinning_fan()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
