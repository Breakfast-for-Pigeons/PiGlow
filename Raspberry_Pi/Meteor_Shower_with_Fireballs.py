################################################################
#                Meteor Shower with Fireballs                  #
################################################################
# Description:                                                 #
# This program lights up the LEDs on arm 1 one at at time then #
# then fades them. Then arm 2. Then arm 3. The code is the     #
# same as the Meteor Shower program, except it randomizes the  #
# brightness of the white LEDs. If the brightness of the white #
# LED is greater than 250, it is considered a fireball meteor  #
# and will print a message to the screen saying "Fireball!"    #
#                                                              #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep
import random

pyglow = PyGlow()

# Initialize
pyglow.all(0)

# Variables
sleep_speed = 0.01

# Functions
def random_brightness():
    return random.randint(0,255)

def shooting_star_1():
    ''' Turn on Arm 1 LEDS and fade '''
    # Turn on A1L1
    pyglow.led(1,60)
    sleep(sleep_speed)
    # Turn on A1L2
    pyglow.led(2,60)
    sleep(sleep_speed)
    # Fade A1L1
    pyglow.led(1,50)
    sleep(sleep_speed)
    # Turn on A1L3
    pyglow.led(3,60)
    sleep(sleep_speed)
    # Fade A1L1 - 2
    pyglow.led(1,40)
    sleep(sleep_speed)
    pyglow.led(2,50)
    sleep(sleep_speed)
    # Turn on A1L4
    pyglow.led(4,60)
    sleep(sleep_speed)
    # Fade A1L1 - 3
    pyglow.led(1,30)
    sleep(sleep_speed)
    pyglow.led(2,40)
    sleep(sleep_speed)
    pyglow.led(3,50)
    sleep(sleep_speed)
    # Turn on A1L5
    pyglow.led(5,60)
    sleep(sleep_speed)
    # Fade A1L1 - 4
    pyglow.led(1,20)
    sleep(sleep_speed)
    pyglow.led(2,30)
    sleep(sleep_speed)
    pyglow.led(3,40)
    sleep(sleep_speed)
    pyglow.led(4,50)
    sleep(sleep_speed)
    # Turn on A1L6, get random brightness
    brightness = random_brightness()
    pyglow.led(6,brightness)
    if brightness > 250:
        print "Fireball!"
    sleep(sleep_speed)
    # Fade A1L1 - 5
    pyglow.led(1,10)
    sleep(sleep_speed)
    pyglow.led(2,20)
    sleep(sleep_speed)
    pyglow.led(3,30)
    sleep(sleep_speed)
    pyglow.led(4,40)
    sleep(sleep_speed)
    pyglow.led(5,50)
    sleep(sleep_speed)
    # Fade A1L1 - 6
    pyglow.led(1, 0)
    sleep(sleep_speed)
    pyglow.led(2,10)
    sleep(sleep_speed)
    pyglow.led(3,20)
    sleep(sleep_speed)
    pyglow.led(4,30)
    sleep(sleep_speed)
    pyglow.led(5,40)
    sleep(sleep_speed)
    pyglow.led(6,50)
    sleep(sleep_speed)
    # Fade A1L2 - 6
    pyglow.led(2,0)
    sleep(sleep_speed)
    pyglow.led(3,10)
    sleep(sleep_speed)
    pyglow.led(4,20)
    sleep(sleep_speed)
    pyglow.led(5,30)
    sleep(sleep_speed)
    pyglow.led(6,40)
    sleep(sleep_speed)
    # Fade A1L3 - 6)
    pyglow.led(3,0)
    sleep(sleep_speed)
    pyglow.led(4,10)
    sleep(sleep_speed)
    pyglow.led(5,20)
    sleep(sleep_speed)
    pyglow.led(6,30)
    sleep(sleep_speed)
    # Fade A1L4 - 6)
    pyglow.led(4,0)
    sleep(sleep_speed)
    pyglow.led(5,10)
    sleep(sleep_speed)
    pyglow.led(6,20)
    sleep(sleep_speed)
    # Fade A1L5 - 6)
    pyglow.led(5, 0)
    sleep(sleep_speed)
    pyglow.led(6,10)
    sleep(sleep_speed)
    # Fade A1L6)
    pyglow.led(6,0)
    sleep(sleep_speed)

    sleep(0.25)

def shooting_star_2():
    ''' Turn on Arm 2 LEDS and fade '''
    # Turn on A2L7
    pyglow.led(7,60)
    sleep(sleep_speed)
    # Turn on A2L8
    pyglow.led(8,60)
    sleep(sleep_speed)
    # Fade A2L7
    pyglow.led(7,50)
    sleep(sleep_speed)
    # Turn on A2L9
    pyglow.led(9,60)
    sleep(sleep_speed)
    # Fade A2L7 - 8
    pyglow.led(7,40)
    sleep(sleep_speed)
    pyglow.led(8,50)
    sleep(sleep_speed)
    # Turn on A2L10
    pyglow.led(10,60)
    sleep(sleep_speed)
    # Fade A2L7 - 9
    pyglow.led(7,30)
    sleep(sleep_speed)
    pyglow.led(8,40)
    sleep(sleep_speed)
    pyglow.led(9,50)
    sleep(sleep_speed)
    # Turn on A2L11
    pyglow.led(11,60)
    sleep(sleep_speed)
    # Fade A2L7 - 10
    pyglow.led(7,20)
    sleep(sleep_speed)
    pyglow.led(8,30)
    sleep(sleep_speed)
    pyglow.led(9,40)
    sleep(sleep_speed)
    pyglow.led(10,50)
    sleep(sleep_speed)
    # Turn on A2L12
    brightness = random_brightness()
    pyglow.led(12,brightness)
    if brightness > 250:
        print "Fireball!"
    sleep(sleep_speed)
    # Fade A2L7 - 11
    pyglow.led(7,10)
    sleep(sleep_speed)
    pyglow.led(8,20)
    sleep(sleep_speed)
    pyglow.led(9,30)
    sleep(sleep_speed)
    pyglow.led(10,40)
    sleep(sleep_speed)
    pyglow.led(11,50)
    sleep(sleep_speed)
    # Fade A2L7 - 12
    pyglow.led(7, 0)
    sleep(sleep_speed)
    pyglow.led(8,10)
    sleep(sleep_speed)
    pyglow.led(9,20)
    sleep(sleep_speed)
    pyglow.led(10,30)
    sleep(sleep_speed)
    pyglow.led(11,40)
    sleep(sleep_speed)
    pyglow.led(12,50)
    sleep(sleep_speed)
    # Fade A2L8 - 12
    pyglow.led(8,0)
    sleep(sleep_speed)
    pyglow.led(9,10)
    sleep(sleep_speed)
    pyglow.led(10,20)
    sleep(sleep_speed)
    pyglow.led(11,30)
    sleep(sleep_speed)
    pyglow.led(12,40)
    sleep(sleep_speed)
    # Fade A2L9 - 12
    pyglow.led(9,0)
    sleep(sleep_speed)
    pyglow.led(10,10)
    sleep(sleep_speed)
    pyglow.led(11,20)
    sleep(sleep_speed)
    pyglow.led(12,30)
    sleep(sleep_speed)
    # Fade A2L10 - 12
    pyglow.led(10,0)
    sleep(sleep_speed)
    pyglow.led(11,10)
    sleep(sleep_speed)
    pyglow.led(12,20)
    sleep(sleep_speed)
    # Fade A2L11 - 12
    pyglow.led(11, 0)
    sleep(sleep_speed)
    pyglow.led(12,10)
    sleep(sleep_speed)
    # Fade A2L12
    pyglow.led(12,0)
    sleep(sleep_speed)

    sleep(0.25)

def shooting_star_3():
    ''' Turn on Arm 3 LEDS and fade '''
    # Turn on A3L13
    pyglow.led(13,60)
    sleep(sleep_speed)
    # Turn on A3L14
    pyglow.led(14,60)
    sleep(sleep_speed)
    # Fade A3L13
    pyglow.led(13,50)
    sleep(sleep_speed)
    # Turn on A3L15
    pyglow.led(15,60)
    sleep(sleep_speed)
    # Fade A3L13 - 14
    pyglow.led(13,40)
    sleep(sleep_speed)
    pyglow.led(14,50)
    sleep(sleep_speed)
    # Turn on A3L16
    pyglow.led(16,60)
    sleep(sleep_speed)
    # Fade A3L13 - 15
    pyglow.led(13,30)
    sleep(sleep_speed)
    pyglow.led(14,40)
    sleep(sleep_speed)
    pyglow.led(15,50)
    sleep(sleep_speed)
    # Turn on A3L17
    pyglow.led(17,60)
    sleep(sleep_speed)
    # Fade A3L13 - 16
    pyglow.led(13,20)
    sleep(sleep_speed)
    pyglow.led(14,30)
    sleep(sleep_speed)
    pyglow.led(15,40)
    sleep(sleep_speed)
    pyglow.led(16,50)
    sleep(sleep_speed)
    # Turn on A3L18
    brightness = random_brightness()
    pyglow.led(18,brightness)
    if brightness > 250:
        print "Fireball!"
    sleep(sleep_speed)
    # Fade A3L13 - 17
    pyglow.led(13,10)
    sleep(sleep_speed)
    pyglow.led(14,20)
    sleep(sleep_speed)
    pyglow.led(15,30)
    sleep(sleep_speed)
    pyglow.led(16,40)
    sleep(sleep_speed)
    pyglow.led(17,50)
    sleep(sleep_speed)
    # Fade A3L13 - 18
    pyglow.led(13, 0)
    sleep(sleep_speed)
    pyglow.led(14,10)
    sleep(sleep_speed)
    pyglow.led(15,20)
    sleep(sleep_speed)
    pyglow.led(16,30)
    sleep(sleep_speed)
    pyglow.led(17,40)
    sleep(sleep_speed)
    pyglow.led(18,50)
    sleep(sleep_speed)
    # Fade A3L14 - 18
    pyglow.led(14,0)
    sleep(sleep_speed)
    pyglow.led(15,10)
    sleep(sleep_speed)
    pyglow.led(16,20)
    sleep(sleep_speed)
    pyglow.led(17,30)
    sleep(sleep_speed)
    pyglow.led(18,40)
    sleep(sleep_speed)
    # Fade A3L15 - 18
    pyglow.led(15,0)
    sleep(sleep_speed)
    pyglow.led(16,10)
    sleep(sleep_speed)
    pyglow.led(17,20)
    sleep(sleep_speed)
    pyglow.led(18,30)
    sleep(sleep_speed)
    # Fade A3L16 - 18
    pyglow.led(16,0)
    sleep(sleep_speed)
    pyglow.led(17,10)
    sleep(sleep_speed)
    pyglow.led(18,20)
    sleep(sleep_speed)
    # Fade A3L17 - 18
    pyglow.led(17, 0)
    sleep(sleep_speed)
    pyglow.led(18,10)
    sleep(sleep_speed)
    # Fade A3L18
    pyglow.led(18,0)
    sleep(sleep_speed)

    sleep(0.25)

# Start the program
try:
    while True:
        # 1, 2, and 3
        shooting_star_1()
        shooting_star_2()
        shooting_star_3()
        # 2, 3, 1
        shooting_star_2()
        shooting_star_3()
        shooting_star_1()
        # 3, 1, 2
        shooting_star_3()
        shooting_star_1()
        shooting_star_2()
        # 1, 3, 2
        shooting_star_1()
        shooting_star_3()
        shooting_star_2()
        # 3, 2, 1
        shooting_star_3()
        shooting_star_2()
        shooting_star_1()
        # 2, 1, 3
        shooting_star_2()
        shooting_star_1()
        shooting_star_3()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
