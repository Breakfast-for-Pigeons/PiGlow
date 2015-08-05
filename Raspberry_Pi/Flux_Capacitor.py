################################################################
#                        Flux Capacitor                        #
################################################################
# Description:                                                 #
# I just took the coolest part from my Spiral Colors program   #
# and gave it its own program. The result reminded me of the   #
# Flux Capacitor from Back To The Future.                      #
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
''' Feel Free to modify the brightness on the following line '''
led_brightness = 100

#Functions
def red_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Red
    pyglow.led(1,led_brightness)
    sleep(sleep_speed)
    pyglow.led(1,0)
    sleep(sleep_speed)
    # Arm 2, Red
    pyglow.led(7,led_brightness)
    sleep(sleep_speed)
    pyglow.led(7,0)
    sleep(sleep_speed)
    # Arm 3, Red
    pyglow.led(13,led_brightness)
    sleep(sleep_speed)
    pyglow.led(13,0)
    sleep(sleep_speed)

def orange_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Orange
    pyglow.led(2,led_brightness)
    sleep(sleep_speed)
    pyglow.led(2,0)
    sleep(sleep_speed)
    # Arm 2, Orange
    pyglow.led(8,led_brightness)
    sleep(sleep_speed)
    pyglow.led(8,0)
    sleep(sleep_speed)
    # Arm 3, Orange
    pyglow.led(14,led_brightness)
    sleep(sleep_speed)
    pyglow.led(14,0)
    sleep(sleep_speed)

def yellow_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Yellow
    pyglow.led(3,led_brightness)
    sleep(sleep_speed)
    pyglow.led(3,0)
    sleep(sleep_speed)
    # Arm 2, Yellow
    pyglow.led(9,led_brightness)
    sleep(sleep_speed)
    pyglow.led(9,0)
    sleep(sleep_speed)
    # Arm 3, Yellow
    pyglow.led(15,led_brightness)
    sleep(sleep_speed)
    pyglow.led(15,0)
    sleep(sleep_speed)

def green_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Green
    pyglow.led(4,led_brightness)
    sleep(sleep_speed)
    pyglow.led(4,0)
    sleep(sleep_speed)
    # Arm 2, Green
    pyglow.led(10,led_brightness)
    sleep(sleep_speed)
    pyglow.led(10,0)
    sleep(sleep_speed)
    # Arm 3, Green
    pyglow.led(16,led_brightness)
    sleep(sleep_speed)
    pyglow.led(16,0)
    sleep(sleep_speed)

def blue_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, Blue
    pyglow.led(5,led_brightness)
    sleep(sleep_speed)
    pyglow.led(5,0)
    sleep(sleep_speed)
    # Arm 2, Blue
    pyglow.led(11,led_brightness)
    sleep(sleep_speed)
    pyglow.led(11,0)
    sleep(sleep_speed)
    # Arm 3, Blue
    pyglow.led(17,led_brightness)
    sleep(sleep_speed)
    pyglow.led(17,0)
    sleep(sleep_speed)

def white_leds(sleep_speed):
    sleep_speed = sleep_speed
    # Arm 1, White
    pyglow.led(6,led_brightness)
    sleep(sleep_speed)
    pyglow.led(6,0)
    sleep(sleep_speed)
    # Arm 2, White
    pyglow.led(12,led_brightness)
    sleep(sleep_speed)
    pyglow.led(12,0)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(18,led_brightness)
    sleep(sleep_speed)
    pyglow.led(18,0)
    sleep(sleep_speed)

def flux_capacitor():
    sleep_speed = 0.01
    red_leds(sleep_speed)
    orange_leds(sleep_speed)
    yellow_leds(sleep_speed)
    green_leds(sleep_speed)
    blue_leds(sleep_speed)
    white_leds(sleep_speed)

# Start the Program
try:  
    while True:
        flux_capacitor()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
