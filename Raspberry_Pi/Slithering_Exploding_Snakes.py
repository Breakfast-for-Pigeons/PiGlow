################################################################
#               Slithering Exploding Snakes                    #
################################################################
# Description:                                                 #
# The title explains it.                                       #
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
sleep_speed = 0.10

# Lists
# LEDs for snakes 12 and 21
snake_12_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18]
# LEDs for snakes 13 and 31
snake_13_leds = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18]
# LEDs for snakes 23 and 32
snake_23_leds = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Functions
def slithering_exploding_snake_12():
    # Light up Snake 12
    '''' Uncomment the following line for feedback '''
    #print "Snake 12 is slithering..."
    pyglow.led(1, 100)
    sleep(sleep_speed)
    pyglow.led(2, 100)
    sleep(sleep_speed)
    pyglow.led(3, 100)
    sleep(sleep_speed)
    pyglow.led(4, 100)
    sleep(sleep_speed)
    pyglow.led(5, 100)
    sleep(sleep_speed)
    pyglow.led(6, 100)
    sleep(sleep_speed)
    pyglow.led(18, 100)
    sleep(sleep_speed)
    pyglow.led(11, 100)
    sleep(sleep_speed)
    pyglow.led(10, 100)
    sleep(sleep_speed)
    pyglow.led(9, 100)
    sleep(sleep_speed)
    pyglow.led(8, 100)
    sleep(sleep_speed)
    pyglow.led(7, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_12_or_21()
    # Explode Snake 12
    '''' Uncomment the following line for feedback '''
    #print "Snake 12 is exploding..."
    explode_snake_12_or_21()

def slithering_exploding_snake_13():
    # Light up Snake 13
    '''' Uncomment the following line for feedback '''
    #print "Snake 13 is slithering..."
    pyglow.led(1, 100)
    sleep(sleep_speed)
    pyglow.led(2, 100)
    sleep(sleep_speed)
    pyglow.led(3, 100)
    sleep(sleep_speed)
    pyglow.led(4, 100)
    sleep(sleep_speed)
    pyglow.led(5, 100)
    sleep(sleep_speed)
    pyglow.led(18, 100)
    sleep(sleep_speed)
    pyglow.led(12, 100)
    sleep(sleep_speed)
    pyglow.led(17, 100)
    sleep(sleep_speed)
    pyglow.led(16, 100)
    sleep(sleep_speed)
    pyglow.led(15, 100)
    sleep(sleep_speed)
    pyglow.led(14, 100)
    sleep(sleep_speed)
    pyglow.led(13, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_13_or_31()
    # Explode Snake 13
    '''' Uncomment the following line for feedback '''
    #print "Snake 13 is exploding..."
    explode_snake_13_or_31()

def slithering_exploding_snake_21():
    # Light up Snake 21
    '''' Uncomment the following line for feedback '''
    #print "Snake 21 is slithering..."
    pyglow.led(7, 100)
    sleep(sleep_speed)
    pyglow.led(8, 100)
    sleep(sleep_speed)
    pyglow.led(9, 100)
    sleep(sleep_speed)
    pyglow.led(10, 100)
    sleep(sleep_speed)
    pyglow.led(11, 100)
    sleep(sleep_speed)
    pyglow.led(18, 100)
    sleep(sleep_speed)
    pyglow.led(6, 100)
    sleep(sleep_speed)
    pyglow.led(5, 100)
    sleep(sleep_speed)
    pyglow.led(4, 100)
    sleep(sleep_speed)
    pyglow.led(3, 100)
    sleep(sleep_speed)
    pyglow.led(2, 100)
    sleep(sleep_speed)
    pyglow.led(1, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_12_or_21()
    # Explode Snake 21
    '''' Uncomment the following line for feedback '''
    #print "Snake 21 is exploding..."
    explode_snake_12_or_21()

def slithering_exploding_snake_23():
    # Light up Snake 23
    '''' Uncomment the following line for feedback '''
    #print "Snake 23 is slithering..."
    pyglow.led(7, 100)
    sleep(sleep_speed)
    pyglow.led(8, 100)
    sleep(sleep_speed)
    pyglow.led(9, 100)
    sleep(sleep_speed)
    pyglow.led(10, 100)
    sleep(sleep_speed)
    pyglow.led(11, 100)
    sleep(sleep_speed)
    pyglow.led(12, 100)
    sleep(sleep_speed)
    pyglow.led(6, 100)
    sleep(sleep_speed)
    pyglow.led(17, 100)
    sleep(sleep_speed)
    pyglow.led(16, 100)
    sleep(sleep_speed)
    pyglow.led(15, 100)
    sleep(sleep_speed)
    pyglow.led(14, 100)
    sleep(sleep_speed)
    pyglow.led(13, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_23_or_32()
    # Explode Snake 23
    '''' Uncomment the following line for feedback '''
    #print "Snake 23 is exploding..."
    explode_snake_23_or_32()
    
def slithering_exploding_snake_31():
    # Light up Snake 31
    '''' Uncomment the following line for feedback '''
    #print "Snake 31 is slithering..."
    pyglow.led(13, 100)
    sleep(sleep_speed)
    pyglow.led(14, 100)
    sleep(sleep_speed)
    pyglow.led(15, 100)
    sleep(sleep_speed)
    pyglow.led(16, 100)
    sleep(sleep_speed)
    pyglow.led(17, 100)
    sleep(sleep_speed)
    pyglow.led(18, 100)
    sleep(sleep_speed)
    pyglow.led(12, 100)
    sleep(sleep_speed)
    pyglow.led(5, 100)
    sleep(sleep_speed)
    pyglow.led(4, 100)
    sleep(sleep_speed)
    pyglow.led(3, 100)
    sleep(sleep_speed)
    pyglow.led(2, 100)
    sleep(sleep_speed)
    pyglow.led(1, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_13_or_31()
    # Explode Snake 31
    '''' Uncomment the following line for feedback '''
    #print "Snake 31 is exploding..."
    explode_snake_13_or_31()

def slithering_exploding_snake_32():
    # Light up Snake 32
    '''' Uncomment the following line for feedback '''
    #print "Snake 32 is slithering..." 
    pyglow.led(13, 100)
    sleep(sleep_speed)
    pyglow.led(14, 100)
    sleep(sleep_speed)
    pyglow.led(15, 100)
    sleep(sleep_speed)
    pyglow.led(16, 100)
    sleep(sleep_speed)
    pyglow.led(17, 100)
    sleep(sleep_speed)
    pyglow.led(6, 100)
    sleep(sleep_speed)
    pyglow.led(12, 100)
    sleep(sleep_speed)
    pyglow.led(11, 100)
    sleep(sleep_speed)
    pyglow.led(10, 100)
    sleep(sleep_speed)
    pyglow.led(9, 100)
    sleep(sleep_speed)
    pyglow.led(8, 100)
    sleep(sleep_speed)
    pyglow.led(7, 100)
    sleep(sleep_speed)
    # Pulse
    pulse_snake_23_or_32()
    # Explode Snake 32
    '''' Uncomment the following line for feedback '''
    #print "Snake 32 is slithering..."
    explode_snake_23_or_32()
    
def pulse_snake_12_or_21():
    # Variable
    pulse_speed = 175
    ''' Uncomment the following print statement for feedback '''
    #print "Snake is pulsing."
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_12_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_12_leds, 100)
    sleep(1)

def pulse_snake_13_or_31():
    # Variable
    pulse_speed = 175
    ''' Uncomment the following print statement for feedback '''
    #print "Snake is pulsing."
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_13_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_13_leds, 100)
    sleep(1)

def pulse_snake_23_or_32():
    # Variable
    pulse_speed = 175
    ''' Uncomment the following print statement for feedback '''
    #print "Snake is pulsing."
    while pulse_speed < 225:
        ''' Uncomment the following print statement for feedback '''
        #print "Pulse speed is: ", pulse_speed
    	pyglow.led(snake_23_leds, 100, speed = pulse_speed, pulse = True)
    	sleep(0)
    	pyglow.update_leds()
        pulse_speed += 1
    pyglow.led(snake_23_leds, 100)
    sleep(1)

def explode_snake_12_or_21():
    # Variables
    explode_speed = 0.020
    # Explode snake 12 or 21
    pyglow.led(18, 0)
    sleep(explode_speed)
    pyglow.led(6, 0)
    sleep(explode_speed)
    pyglow.led(11, 0)
    sleep(explode_speed)
    pyglow.led(5, 0)
    sleep(explode_speed)
    pyglow.led(10, 0)
    sleep(explode_speed)
    pyglow.led(4, 0)
    sleep(explode_speed)
    pyglow.led(9, 0)
    sleep(explode_speed)
    pyglow.led(3, 0)
    sleep(explode_speed)
    pyglow.led(8, 0)
    sleep(explode_speed)
    pyglow.led(2, 0)
    sleep(explode_speed)
    pyglow.led(7, 0)
    sleep(explode_speed)
    pyglow.led(1, 0)
    sleep(explode_speed)

def explode_snake_13_or_31():
    # Variables
    explode_speed = 0.020
    # Explode snake 13 or 31
    pyglow.led(18, 0)
    sleep(explode_speed)
    pyglow.led(12, 0)
    sleep(explode_speed)
    pyglow.led(17, 0)
    sleep(explode_speed)
    pyglow.led(5, 0)
    sleep(explode_speed)
    pyglow.led(16, 0)
    sleep(explode_speed)
    pyglow.led(4, 0)
    sleep(explode_speed)
    pyglow.led(15, 0)
    sleep(explode_speed)
    pyglow.led(3, 0)
    sleep(explode_speed)
    pyglow.led(14, 0)
    sleep(explode_speed)
    pyglow.led(2, 0)
    sleep(explode_speed)
    pyglow.led(13, 0)
    sleep(explode_speed)
    pyglow.led(1, 0)
    sleep(explode_speed)

def explode_snake_23_or_32():
    # Variables
    explode_speed = 0.020
    # Explode snake 23 or 32
    pyglow.led(12, 0)
    sleep(explode_speed)
    pyglow.led(6, 0)
    sleep(explode_speed)
    pyglow.led(17, 0)
    sleep(explode_speed)
    pyglow.led(11, 0)
    sleep(explode_speed)
    pyglow.led(16, 0)
    sleep(explode_speed)
    pyglow.led(10, 0)
    sleep(explode_speed)
    pyglow.led(15, 0)
    sleep(explode_speed)
    pyglow.led(9, 0)
    sleep(explode_speed)
    pyglow.led(14, 0)
    sleep(explode_speed)
    pyglow.led(8, 0)
    sleep(explode_speed)
    pyglow.led(13, 0)
    sleep(explode_speed)
    pyglow.led(7, 0)
    sleep(explode_speed)

# Start the program
try:
    while True:
        # Snakes 12, 13, 21, 23, 31, 32
        slithering_exploding_snake_12()
        sleep(1)
        slithering_exploding_snake_13()
        sleep(1)
        slithering_exploding_snake_21()
        sleep(1)
        slithering_exploding_snake_23()
        sleep(1)
        slithering_exploding_snake_31()
        sleep(1)
        slithering_exploding_snake_32()
        sleep(1)
        # Snakes 12, 23, 31, 13, 32, 21
        slithering_exploding_snake_12()
        sleep(1)
        slithering_exploding_snake_23()
        sleep(1)
        slithering_exploding_snake_31()
        sleep(1)
        slithering_exploding_snake_13()
        sleep(1)
        slithering_exploding_snake_32()
        sleep(1)
        slithering_exploding_snake_21()
        sleep(1)
        # Snakes 13, 12, 23, 21, 31, 32
        slithering_exploding_snake_13()
        sleep(1)
        slithering_exploding_snake_12()
        sleep(1)
        slithering_exploding_snake_23()
        sleep(1)
        slithering_exploding_snake_21()
        sleep(1)
        slithering_exploding_snake_31()
        sleep(1)
        slithering_exploding_snake_32()
        sleep(1)
        # Snakes 13, 32, 21, 12, 23, 31
        slithering_exploding_snake_13()
        sleep(1)
        slithering_exploding_snake_32()
        sleep(1)
        slithering_exploding_snake_21()
        sleep(1)
        slithering_exploding_snake_12()
        sleep(1)
        slithering_exploding_snake_23()
        sleep(1)
        slithering_exploding_snake_31()
        sleep(1)
# Stop the exploding snake carnage with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
