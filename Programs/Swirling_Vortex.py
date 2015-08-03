################################################################
#                     Swiriling Vortex                         #
################################################################
# Description:                                                 #
# This program lights up the LEDs on one at at time then       #
# then fades them. Like "Zoom Zoom Zoom" except all 3 arms     #
# are done at the same time.                                   #
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
sleep_speed = 0.01

# Functions
def zoom_in():
    # Turn on red
    pyglow.color("red", 60)
    sleep(sleep_speed)
    # Turn on orange
    pyglow.color("orange", 60)
    sleep(sleep_speed)
    # Fade red
    pyglow.color("red", 50)
    sleep(sleep_speed)
    # Turn on yellow
    pyglow.color("yellow", 60)
    sleep(sleep_speed)
    # Fade red and orange
    pyglow.color("red", 40)
    sleep(sleep_speed)
    pyglow.color("orange", 50)
    sleep(sleep_speed)
    # Turn on green
    pyglow.color("green", 60)
    sleep(sleep_speed)
    # Fade red, orange, and yellow
    pyglow.color("red", 30)
    sleep(sleep_speed)
    pyglow.color("orange", 40)
    sleep(sleep_speed)
    pyglow.color("yellow", 50)
    sleep(sleep_speed)
    # Turn on blue
    pyglow.color("blue", 60)
    sleep(sleep_speed)
    # Fade red, orange, yellow, green
    pyglow.color("red", 20)
    sleep(sleep_speed)
    pyglow.color("orange", 30)
    sleep(sleep_speed)
    pyglow.color("yellow", 40)
    sleep(sleep_speed)
    pyglow.color("green", 50)
    sleep(sleep_speed)
    # Turn on white
    pyglow.color("white", 60)
    sleep(sleep_speed)
    # Fade red, orange, yellow, green, and blue
    pyglow.color("red", 10)
    sleep(sleep_speed)
    pyglow.color("orange", 20)
    sleep(sleep_speed)
    pyglow.color("yellow", 30)
    sleep(sleep_speed)
    pyglow.color("green", 40)
    sleep(sleep_speed)
    pyglow.color("blue", 50)
    sleep(sleep_speed)
    # Fade all
    pyglow.color("red", 0)
    sleep(sleep_speed)
    pyglow.color("orange", 10)
    sleep(sleep_speed)
    pyglow.color("yellow", 20)
    sleep(sleep_speed)
    pyglow.color("green", 30)
    sleep(sleep_speed)
    pyglow.color("blue", 40)
    sleep(sleep_speed)
    pyglow.color("white", 50)
    sleep(sleep_speed)
    # Fade orange, yellow, green, blue, and white
    pyglow.color("orange", 0)
    sleep(sleep_speed)
    pyglow.color("yellow", 10)
    sleep(sleep_speed)
    pyglow.color("green", 20)
    sleep(sleep_speed)
    pyglow.color("blue", 30)
    sleep(sleep_speed)
    pyglow.color("white", 40)
    sleep(sleep_speed)
    # Fade yellow, green, blue, and white
    pyglow.color("yellow", 0)
    sleep(sleep_speed)
    pyglow.color("green", 10)
    sleep(sleep_speed)
    pyglow.color("blue", 20)
    sleep(sleep_speed)
    pyglow.color("white", 30)
    sleep(sleep_speed)
    # Fade green, blue, and white
    pyglow.color("green", 0)
    sleep(sleep_speed)
    pyglow.color("blue", 10)
    sleep(sleep_speed)
    pyglow.color("white", 20)
    sleep(sleep_speed)
    # Fade blue, and white
    pyglow.color("blue", 0)
    sleep(sleep_speed)
    pyglow.color("white", 10)
    sleep(sleep_speed)
    # Fade white
    pyglow.color("white", 0)
    sleep(sleep_speed)
   
while True:
    zoom_in()
    sleep(1)
