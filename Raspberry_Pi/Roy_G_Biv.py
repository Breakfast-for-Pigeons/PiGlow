################################################################
#                        Roy G. Biv                            #
################################################################
# Description:                                                 #
# This program lights up like colors one at the same,          #
# all red, all orange, etc... then gradually increases the     #
# speed and then goes through the entire process again.        #                                        #
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
counter = 5
sleep_speed = 0.25

# Functions
def roy_g_biv(sleep_speed):
    pyglow.color("red",100)
    sleep(sleep_speed)
    pyglow.color("red",0)
    pyglow.color("orange",100)
    sleep(sleep_speed)
    pyglow.color("orange",0)
    pyglow.color("yellow",100)
    sleep(sleep_speed)
    pyglow.color("yellow",0)
    pyglow.color("green",100)
    sleep(sleep_speed)
    pyglow.color("green",0)
    pyglow.color("blue",100)
    sleep(sleep_speed)
    pyglow.color("blue",0)
    pyglow.color("white",100)
    sleep(sleep_speed)
    pyglow.color("white",0) 
    
def increase_speed():
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Increasing speed..."
    sleep_speed = 0.25
    while sleep_speed > 0.05:
        ''' Uncomment the following line for feedback while the program is running '''
        # print "The speed is now: ", sleep_speed
        roy_g_biv(sleep_speed)
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
        roy_g_biv(sleep_speed)
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
        roy_g_biv(sleep_speed)
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
        roy_g_biv(sleep_speed)
        # decrease counter
        counter -= 1
    sleep(2)
    increase_speed()

#Start the program
try:
    increase_speed()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
