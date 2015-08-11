################################################################
#                          Confluence                          #
################################################################
# Description:                                                 #
# This program is basically my "Light the Fuse" program in     #
# reverse. It lights up 2 arms at once and converges into the  #
# third arm.                                                   #
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
def confluence_2_and_3_into_1(sleep_speed):
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence 2 and 3 into 1..."
    # Arm 2 and 3, Red
    pyglow.led(7,120)
    pyglow.led(13,120)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    pyglow.led(8,120)
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    pyglow.led(9,120)
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    pyglow.led(10,120)
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    pyglow.led(11,120)
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    pyglow.led(12,120)
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Arm 1, White
    pyglow.led(6,120)
    sleep(sleep_speed)
    # Arm 1, Blue
    pyglow.led(5,120)
    sleep(sleep_speed)
    # Arm 1, Green
    pyglow.led(4,120)
    sleep(sleep_speed)
    # Arm 1, Yellow
    pyglow.led(3,120)
    sleep(sleep_speed)
    # Arm 1, Orange
    pyglow.led(2,120)
    sleep(sleep_speed)
    # Arm 1, Red
    pyglow.led(1,120)
    sleep(sleep_speed)
    sleep(1)
    # Turn 'em off
    pyglow.all(0)
    sleep(1)

def confluence_1_and_3_into_2(sleep_speed):
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence 1 and 3 into 2..."
    # Arm 1 and 3, Red
    pyglow.led(1,120)
    pyglow.led(13,120)
    sleep(sleep_speed)   
    # Arm 1 and 3, Orange
    pyglow.led(2,120)
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    pyglow.led(3,120)
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    pyglow.led(4,120)
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    pyglow.led(5,120)
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    pyglow.led(6,120)
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,120)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,120)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,120)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,120)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,120)
    sleep(sleep_speed)
    # Arm 2, Red
    pyglow.led(7,120)
    sleep(sleep_speed)
    sleep(1)
    # Turn 'em off
    pyglow.all(0)
    sleep(1)

def confluence_1_and_2_into_3(sleep_speed):
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence 1 and 2 into 3..."
    # Arm 1 and 2, Red
    pyglow.led(1,120)
    pyglow.led(7,120)
    # Arm 1 and 2, Orange
    pyglow.led(2,120)
    pyglow.led(8,120)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    pyglow.led(3,120)
    pyglow.led(9,120)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    pyglow.led(4,120)
    pyglow.led(10,120)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    pyglow.led(5,120)
    pyglow.led(11,120)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    pyglow.led(6,120)
    pyglow.led(12,120)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Arm 3, Red
    pyglow.led(13,120)
    sleep(sleep_speed)
    sleep(1)
    # Turn 'em off
    pyglow.all(0)
    sleep(1)
    
def confluence():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence"
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "The speed is now: ", sleep_speed
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # Increase speed
        sleep_speed -= 0.05
    go_fast(sleep_speed)

def go_fast(sleep_speed):
    sleep_speed = 0.05
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going fast..."
    while sleep_speed > 0.01:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "sleep_speed = ", sleep_speed
        confluence_2_and_3_into_1(sleep_speed)
        confluence_1_and_3_into_2(sleep_speed)
        confluence_1_and_2_into_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025
    confluence()
    
# Start the Program
try:
   confluence()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
