################################################################
#                     Rippling Confluence                      #
################################################################
# Description:                                                 #
# This program does the same thing as the Confluence program,  #
# but it also creates "ripples" by dimming the brightness of   #
# the LEDs one at a time.                                      #
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
    # Variables
    sleep_speed = sleep_speed
    counter = 10 
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
    while counter > 0:
        rippling_confluence_1(sleep_speed)
        counter -= 1
    # Turn 'em off one at a time
    # Arm 2 and 3, Red
    pyglow.led(7,0)
    pyglow.led(13,0)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    pyglow.led(8,0)
    pyglow.led(14,0)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    pyglow.led(9,0)
    pyglow.led(15,0)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    pyglow.led(10,0)
    pyglow.led(16,0)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    pyglow.led(11,0)
    pyglow.led(17,0)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    pyglow.led(12,0)
    pyglow.led(18,0)
    sleep(sleep_speed)
    # Arm 1, White
    pyglow.led(6,0)
    sleep(sleep_speed)
    # Arm 1, Blue
    pyglow.led(5,0)
    sleep(sleep_speed)
    # Arm 1, Green
    pyglow.led(4,0)
    sleep(sleep_speed)
    # Arm 1, Yellow
    pyglow.led(3,0)
    sleep(sleep_speed)
    # Arm 1, Orange
    pyglow.led(2,0)
    sleep(sleep_speed)
    # Arm 1, Red
    pyglow.led(1,0)
    sleep(sleep_speed)
    # Pause before next function
    sleep(1)

def confluence_1_and_3_into_2(sleep_speed):
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence 1 and 3 into 2..."
    # Variables
    sleep_speed = sleep_speed
    counter = 10 
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
    while counter > 0:
        rippling_confluence_2(sleep_speed)
        counter -= 1
    # Arm 1 and 3, Red
    pyglow.led(1,0)
    pyglow.led(13,0)
    sleep(sleep_speed)   
    # Arm 1 and 3, Orange
    pyglow.led(2,0)
    pyglow.led(14,0)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    pyglow.led(3,0)
    pyglow.led(15,0)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    pyglow.led(4,0)
    pyglow.led(16,0)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    pyglow.led(5,0)
    pyglow.led(17,0)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    pyglow.led(6,0)
    pyglow.led(18,0)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,0)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,0)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,0)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,0)
    sleep(sleep_speed)
    # Arm 2, Red
    pyglow.led(7,0)
    sleep(sleep_speed)
    sleep(1)

def confluence_1_and_2_into_3(sleep_speed):
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Confluence 1 and 2 into 3..."
    # Variables
    sleep_speed = sleep_speed
    counter = 10 
    # Arm 1 and 2, Red
    pyglow.led(1,120)
    pyglow.led(7,120)
    sleep(sleep_speed)
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
    while counter > 0:
        rippling_confluence_3(sleep_speed)
        counter -= 1
    # Arm 1 and 2, Red
    pyglow.led(1,0)
    pyglow.led(7,0)
    # Arm 1 and 2, Orange
    pyglow.led(2,0)
    pyglow.led(8,0)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    pyglow.led(3,0)
    pyglow.led(9,0)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    pyglow.led(4,0)
    pyglow.led(10,0)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    pyglow.led(5,0)
    pyglow.led(11,0)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    pyglow.led(6,0)
    pyglow.led(12,0)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(18,0)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(17,0)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(16,0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(15,0)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(14,0)
    sleep(sleep_speed)
    # Arm 3, Red
    pyglow.led(13,0)
    sleep(sleep_speed)
    sleep(1)

def rippling_confluence_1(sleep_speed): 
    # Variables
    ripple_speed = 0.05
    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05
    #print "ripple speed is:", ripple_speed
    # Ripple
    # Arm 2 and 3, Red
    pyglow.led(7,60)
    pyglow.led(13,60)
    sleep(ripple_speed)
    # Arm 2 and 3, Red
    pyglow.led(7,120)
    pyglow.led(13,120)
    sleep(ripple_speed)
    # Arm 2 and 3, Orange
    pyglow.led(8,60)
    pyglow.led(14,60)
    sleep(ripple_speed)
    pyglow.led(8,120)
    pyglow.led(14,120)
    sleep(ripple_speed)
    # Arm 2 and 3, Yellow
    pyglow.led(9,60)
    pyglow.led(15,60)
    sleep(ripple_speed)
    pyglow.led(9,120)
    pyglow.led(15,120)
    sleep(ripple_speed)
    # Arm 2 and 3, Green
    pyglow.led(10,60)
    pyglow.led(16,60)
    sleep(ripple_speed)
    pyglow.led(10,120)
    pyglow.led(16,120)
    sleep(ripple_speed)
    # Arm 2 and 3, Blue
    pyglow.led(11,60)
    pyglow.led(17,60)
    sleep(ripple_speed)
    pyglow.led(11,120)
    pyglow.led(17,120)
    sleep(ripple_speed)
    # Arm 2 and 3, White
    pyglow.led(12,60)
    pyglow.led(18,60)
    sleep(ripple_speed)
    pyglow.led(12,120)
    pyglow.led(18,120)
    sleep(ripple_speed)
    # Arm 1, White
    pyglow.led(6,60)
    sleep(ripple_speed)
    pyglow.led(6,120)
    sleep(ripple_speed)
    # Arm 1, Blue
    pyglow.led(5,60)
    sleep(ripple_speed)
    pyglow.led(5,120)
    sleep(ripple_speed)
    # Arm 1, Green
    pyglow.led(4,60)
    sleep(ripple_speed)
    pyglow.led(4,120)
    sleep(ripple_speed)
    # Arm 1, Yellow
    pyglow.led(3,60)
    sleep(ripple_speed)
    pyglow.led(3,120)
    sleep(ripple_speed)
    # Arm 1, Orange
    pyglow.led(2,80)
    sleep(ripple_speed)
    pyglow.led(2,120)
    sleep(ripple_speed)
    # Arm 1, Red
    pyglow.led(1,60)
    sleep(ripple_speed)
    pyglow.led(1,120)
    sleep(ripple_speed)

def rippling_confluence_2(sleep_speed):
    # Variables
    ripple_speed = 0.05
    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05
    #print "ripple speed is:", ripple_speed
    #Ripple
    # Arm 1 and 3, Red
    pyglow.led(1,60)
    pyglow.led(13,60)
    sleep(ripple_speed)
    pyglow.led(1,120)
    pyglow.led(13,120)
    sleep(ripple_speed)  
    # Arm 1 and 3, Orange
    pyglow.led(2,60)
    pyglow.led(14,60)
    sleep(ripple_speed)
    pyglow.led(2,120)
    pyglow.led(14,120)
    sleep(ripple_speed)
    # Arm 1 and 3, Yellow
    pyglow.led(3,60)
    pyglow.led(15,60)
    sleep(ripple_speed)
    pyglow.led(3,120)
    pyglow.led(15,120)
    sleep(ripple_speed)
    # Arm 1 and 3, Green
    pyglow.led(4,60)
    pyglow.led(16,60)
    sleep(ripple_speed)
    pyglow.led(4,120)
    pyglow.led(16,120)
    sleep(ripple_speed)
    # Arm 1 and 3, Blue
    pyglow.led(5,60)
    pyglow.led(17,60)
    sleep(ripple_speed)
    pyglow.led(5,120)
    pyglow.led(17,120)
    sleep(ripple_speed)
    # Arm 1 and 3, White
    pyglow.led(6,60)
    pyglow.led(18,60)
    sleep(ripple_speed)
    pyglow.led(6,120)
    pyglow.led(18,120)
    sleep(ripple_speed)
    # Arm 2, White
    pyglow.led(12,60)
    sleep(ripple_speed)
    pyglow.led(12,120)
    sleep(ripple_speed)
    # Arm 2, Blue
    pyglow.led(11,60)
    sleep(ripple_speed)
    pyglow.led(11,120)
    sleep(ripple_speed)
    # Arm 2, Green
    pyglow.led(10,60)
    sleep(ripple_speed)
    pyglow.led(10,120)
    sleep(ripple_speed)
    # Arm 2, Yellow
    pyglow.led(9,60)
    sleep(ripple_speed)
    pyglow.led(9,120)
    sleep(ripple_speed)
    # Arm 2, Orange
    pyglow.led(8,60)
    sleep(ripple_speed)
    pyglow.led(8,120)
    sleep(ripple_speed)
    # Arm 2, Red
    pyglow.led(7,60)
    sleep(ripple_speed)
    pyglow.led(7,120)
    sleep(ripple_speed)

def rippling_confluence_3(sleep_speed):
    # Variables
    ripple_speed = 0.05
    if sleep_speed < ripple_speed:
        ripple_speed = sleep_speed
    else:
        ripple_speed = 0.05
    #print "ripple speed is:", ripple_speed
    #Ripple
    # Arm 1 and 2, Red
    pyglow.led(1,60)
    pyglow.led(7,60)
    sleep(ripple_speed)
    pyglow.led(1,120)
    pyglow.led(7,120)
    sleep(ripple_speed)
    # Arm 1 and 2, Orange
    pyglow.led(2,60)
    pyglow.led(8,60)
    sleep(ripple_speed)
    pyglow.led(2,120)
    pyglow.led(8,120)
    sleep(ripple_speed)
    # Arm 1 and 2, Yellow
    pyglow.led(3,60)
    pyglow.led(9,60)
    sleep(ripple_speed)
    pyglow.led(3,120)
    pyglow.led(9,120)
    sleep(ripple_speed)
    # Arm 1 and 2, Green
    pyglow.led(4,60)
    pyglow.led(10,60)
    sleep(ripple_speed)
    pyglow.led(4,120)
    pyglow.led(10,120)
    sleep(ripple_speed)
    # Arm 1 and 2, Blue
    pyglow.led(5,60)
    pyglow.led(11,60)
    sleep(ripple_speed)
    pyglow.led(5,120)
    pyglow.led(11,120)
    sleep(ripple_speed)
    # Arm 1 and 2, White
    pyglow.led(6,60)
    pyglow.led(12,60)
    sleep(ripple_speed)
    pyglow.led(6,120)
    pyglow.led(12,120)
    sleep(ripple_speed)
    # Arm 3, White
    pyglow.led(18,60)
    sleep(ripple_speed)
    pyglow.led(18,120)
    sleep(ripple_speed)
    # Arm 3, Blue
    pyglow.led(17,60)
    sleep(ripple_speed)
    pyglow.led(17,120)
    sleep(ripple_speed)
    # Arm 3, Green
    pyglow.led(16,60)
    sleep(ripple_speed)
    pyglow.led(16,120)
    sleep(ripple_speed)
    # Arm 3, Yellow
    pyglow.led(15,60)
    sleep(ripple_speed)
    pyglow.led(15,120)
    sleep(ripple_speed)
    # Arm 3, Orange
    pyglow.led(14,60)
    sleep(ripple_speed)
    pyglow.led(14,120)
    sleep(ripple_speed)
    # Arm 3, Red
    pyglow.led(13,60)
    sleep(ripple_speed)
    pyglow.led(13,120)
    sleep(ripple_speed)

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
    sleep(2)
    confluence()
    
# Start the Program
try:
   confluence()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()