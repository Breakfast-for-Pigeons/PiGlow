################################################################
#                            Fireworks                         #
################################################################
# Description:                                                 #
# This program lights up the LEDs on one at at time then       #
# then fades them, starting from the center white LEDs and     #
# moving outward to the red LEDs. The result looks like        #
# fireworks.
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
sleep_speed = 0.025

# Functions
def fireworks():
    # Turn on white
    pyglow.color("white",60)
    sleep(sleep_speed)
    # Turn on blue
    pyglow.color("blue",60)
    sleep(sleep_speed)
    # Fade white
    pyglow.color("white",50)
    sleep(sleep_speed)
    # Turn on green
    pyglow.color("green",60)
    sleep(sleep_speed)
    # Fade white and blue
    pyglow.color("white",40)
    sleep(sleep_speed)
    pyglow.color("blue",50)
    sleep(sleep_speed)
    # Turn on yellow
    pyglow.color("yellow",60)
    sleep(sleep_speed)
    # Fade white, blue, and green
    pyglow.color("white",30)
    sleep(sleep_speed)
    pyglow.color("blue",40)
    sleep(sleep_speed)
    pyglow.color("green",50)
    sleep(sleep_speed)
    # Turn on orange
    pyglow.color("orange",60)
    sleep(sleep_speed)
    # Fade white, blue, green, and yellow
    pyglow.color("white",20)
    sleep(sleep_speed)
    pyglow.color("blue",30)
    sleep(sleep_speed)
    pyglow.color("green",40)
    sleep(sleep_speed)
    pyglow.color("yellow",50)
    sleep(sleep_speed)
    # Turn on red
    pyglow.color("red",60)
    sleep(sleep_speed)
    # Fade white, blue, green, yellow, and orange
    pyglow.color("white",10)
    sleep(sleep_speed)
    pyglow.color("blue",20)
    sleep(sleep_speed)
    pyglow.color("green",30)
    sleep(sleep_speed)
    pyglow.color("yellow",40)
    sleep(sleep_speed)
    pyglow.color("orange",50)
    sleep(sleep_speed)
    # Fade all
    pyglow.color("white",0)
    sleep(sleep_speed)
    pyglow.color("blue",10)
    sleep(sleep_speed)
    pyglow.color("green",20)
    sleep(sleep_speed)
    pyglow.color("yellow",30)
    sleep(sleep_speed)
    pyglow.color("orange",40)
    sleep(sleep_speed)
    pyglow.color("red",50)
    sleep(sleep_speed)
    # Fade blue, green, yellow, orange, and red
    pyglow.color("blue",0)
    sleep(sleep_speed)
    pyglow.color("green",10)
    sleep(sleep_speed)
    pyglow.color("yellow",20)
    sleep(sleep_speed)
    pyglow.color("orange",30)
    sleep(sleep_speed)
    pyglow.color("red",40)
    sleep(sleep_speed)
    # Fade green, yellow, orange, and red
    pyglow.color("green",0)
    sleep(sleep_speed)
    pyglow.color("yellow",10)
    sleep(sleep_speed)
    pyglow.color("orange",20)
    sleep(sleep_speed)
    pyglow.color("red",30)
    sleep(sleep_speed)
    # Fade yellow, orange, and red
    pyglow.color("yellow",0)
    sleep(sleep_speed)
    pyglow.color("orange",10)
    sleep(sleep_speed)
    pyglow.color("red",20)
    sleep(sleep_speed)
    # Fade orange, and red
    pyglow.color("orange",0)
    sleep(sleep_speed)
    pyglow.color("red",10)
    sleep(sleep_speed)
    # Fade red
    pyglow.color("red",0)
    sleep(sleep_speed)
    
    sleep(1)
    
# Start fireworks
try:
    while True:
        fireworks()
# Stop the fireworks and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
