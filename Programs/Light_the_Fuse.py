################################################################
#                       Light the Fuse                         #
################################################################
# Description:                                                 #
# This program lights up arm 1, then lights up arms 2 and 3    #
# at the same time. Then lights up arm 2, which then lights    #
# up arms 1 and 3. Then lights up arm 3, which then lights     #
# up arms 1 and 2.  Then goes through the whole thing again    #
# while increasing the speed.                                  #
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
#sleep_speed = 0.25

def light_fuse_1(sleep_speed): 
    # Arm 1, Red
    pyglow.led(1,100)
    sleep(sleep_speed)
    # Arm 1, Orange
    pyglow.led(2,100)
    sleep(sleep_speed)
    # Arm 1, Yellow
    pyglow.led(3,100)
    sleep(sleep_speed)
    # Arm 1, Green
    pyglow.led(4,100)
    sleep(sleep_speed)
    # Arm 1, Blue
    pyglow.led(5,100)
    sleep(sleep_speed)
    # Arm 1, White
    pyglow.led(6,100)
    sleep(sleep_speed)
    # Arm 2 and 3, White
    pyglow.led(12,100)
    pyglow.led(18,100)
    sleep(sleep_speed)
    # Arm 2 and 3, Blue
    pyglow.led(11,100)
    pyglow.led(17,100)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    pyglow.led(10,100)
    pyglow.led(16,100)
    sleep(sleep_speed)
    # Arm 2 and 3, Yellow
    pyglow.led(9,100)
    pyglow.led(15,100)
    sleep(sleep_speed)
    # Arm 2 and 3, Orange
    pyglow.led(8,100)
    pyglow.led(14,100)
    sleep(sleep_speed)
    # Arm 2 and 3, Red
    pyglow.led(7,100)
    pyglow.led(13,100)
    sleep(sleep_speed)
    # Turn 'em off
    pyglow.all(0)

def light_fuse_2(sleep_speed):
    # Arm 2, Red
    pyglow.led(7,100)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,100)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,100)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,100)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,100)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,100)
    sleep(sleep_speed)
    # Arm 1 and 3, White
    pyglow.led(6,100)
    pyglow.led(18,100)
    sleep(sleep_speed)
    # Arm 1 and 3, Blue
    pyglow.led(5,100)
    pyglow.led(17,100)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    pyglow.led(4,100)
    pyglow.led(16,100)
    sleep(sleep_speed)
    # Arm 1 and 3, Yellow
    pyglow.led(3,100)
    pyglow.led(15,100)
    sleep(sleep_speed)
    # Arm 1 and 3, Orange
    pyglow.led(2,100)
    pyglow.led(14,100)
    sleep(sleep_speed)
    # Arm 1 and 3, Red
    pyglow.led(1,100)
    pyglow.led(13,100)
    sleep(sleep_speed)
    # Turn 'em off
    pyglow.all(0)

def light_fuse_3(sleep_speed):
    # Arm 3, Red
    pyglow.led(13,100)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(14,100)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(15,100)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(16,100)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(17,100)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(18,100)
    sleep(sleep_speed)
    # Arm 1 and 2, White
    pyglow.led(6,100)
    pyglow.led(12,100)
    sleep(sleep_speed)
    # Arm 1 and 2, Blue
    pyglow.led(5,100)
    pyglow.led(11,100)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    pyglow.led(4,100)
    pyglow.led(10,100)
    sleep(sleep_speed)
    # Arm 1 and 2, Yellow
    pyglow.led(3,100)
    pyglow.led(9,100)
    sleep(sleep_speed)
    # Arm 1 and 2, Orange
    pyglow.led(2,100)
    pyglow.led(8,100)
    sleep(sleep_speed)
    # Arm 1 and 2, Red
    pyglow.led(1,100)
    pyglow.led(7,100)
    sleep(sleep_speed)
    #Turn 'em off
    pyglow.all(0)

def light_the_fuse():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Light the Fuse"
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "The speed is now: ", sleep_speed
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
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
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025
    go_faster()

def go_faster():
    sleep_speed = 0.01
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going faster..."
    counter = 10
    while counter > 0:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "sleep_speed = ", sleep_speed#print "counter = ", counter
        light_fuse_1(sleep_speed)
        light_fuse_2(sleep_speed)
        light_fuse_3(sleep_speed)
        # decrease counter
        counter -= 1
    sleep(2)
    light_the_fuse()
    
# Start the Program
light_the_fuse()
