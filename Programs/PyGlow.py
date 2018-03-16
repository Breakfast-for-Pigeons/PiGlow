#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# For more information and documentation see:
# https://github.com/benleb/PYGlow
#
#####
#
# Author:
#
# Ben Lebherz (@ben_leb)
#
# Contributors:
#
# Austin Parker (@austinlparker)
#  - pulse features
# Jon@Pimoroni
#  - gamma correction mapping
# Jiri Tyr
#  - PEP8 code compliance
#  - code refactoring
#  - updated project documentation
#  - improvements of the pulse function
#  - removed the redundant pulse_* methods
#
#####

# Import some modules
from smbus import SMBus
from time import sleep
import RPi.GPIO as rpi
import re


# Define GPIO addresses
I2C_ADDR = 0x54
EN_OUTPUT_ADDR = 0x00
EN_ARM1_ADDR = 0x13
EN_ARM2_ADDR = 0x14
EN_ARM3_ADDR = 0x15
UPD_PWM_ADDR = 0x16

# Pulse direction
UP = 1
DOWN = -1
BOTH = 0

# Define global variables
LED_LIST = tuple(xrange(1, 19))
LED_HEX_LIST = (
    0x07, 0x08, 0x09, 0x06, 0x05, 0x0A,
    0x12, 0x11, 0x10, 0x0E, 0x0C, 0x0B,
    0x01, 0x02, 0x03, 0x04, 0x0F, 0x0D)
ARM_LIST = tuple(xrange(1, 4))
ARM_LED_LIST = map(tuple, (xrange(1, 7), xrange(7, 13), xrange(13, 19)))
COLOR_LIST = tuple(xrange(1, 7))
COLOR_NAME_LIST = ("white", "blue", "green", "yellow", "orange", "red")
COLOR_LED_LIST = (
    (6, 12, 18), (5, 11, 17), (4, 10, 16), (3, 9, 15), (2, 8, 14), (1, 7, 13))
GAMMA_TABLE = (
    0, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 5, 5, 5, 5, 5,
    5, 5, 5, 6, 6, 6, 6, 6,
    6, 6, 7, 7, 7, 7, 7, 7,
    8, 8, 8, 8, 8, 8, 9, 9,
    9, 9, 10, 10, 10, 10, 10, 11,
    11, 11, 11, 12, 12, 12, 13, 13,
    13, 13, 14, 14, 14, 15, 15, 15,
    16, 16, 16, 17, 17, 18, 18, 18,
    19, 19, 20, 20, 20, 21, 21, 22,
    22, 23, 23, 24, 24, 25, 26, 26,
    27, 27, 28, 29, 29, 30, 31, 31,
    32, 33, 33, 34, 35, 36, 36, 37,
    38, 39, 40, 41, 42, 42, 43, 44,
    45, 46, 47, 48, 50, 51, 52, 53,
    54, 55, 57, 58, 59, 60, 62, 63,
    64, 66, 67, 69, 70, 72, 74, 75,
    77, 79, 80, 82, 84, 86, 88, 90,
    91, 94, 96, 98, 100, 102, 104, 107,
    109, 111, 114, 116, 119, 122, 124, 127,
    130, 133, 136, 139, 142, 145, 148, 151,
    155, 158, 161, 165, 169, 172, 176, 180,
    184, 188, 192, 196, 201, 205, 210, 214,
    219, 224, 229, 234, 239, 244, 250, 255)


class PyGlow:
    def __init__(
            self,
            brightness=None, speed=None, pulse=None, pulse_dir=None):

        # Check what Raspberry Pi version we got
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2 or rpi.RPI_REVISION == 3:
            i2c_bus = 1
        else:
            raise PyGlowException(
                self, "Unknown Raspberry Pi hardware revision: %s" %
                (rpi.RPI_REVISION))

        # Enables the LEDs
        self.bus = SMBus(i2c_bus)

        # Tell the SN3218 to enable output
        self.bus.write_byte_data(I2C_ADDR, EN_OUTPUT_ADDR, 0x01)

        # Enable each LED arm
        self.bus.write_byte_data(I2C_ADDR, EN_ARM1_ADDR, 0xFF)
        self.bus.write_byte_data(I2C_ADDR, EN_ARM2_ADDR, 0xFF)
        self.bus.write_byte_data(I2C_ADDR, EN_ARM3_ADDR, 0xFF)

        # Set default brightness and pulsing params
        self.brightness = brightness
        self.speed = speed
        self.pulse = pulse
        self.pulse_dir = pulse_dir

        # Define the LED state variable
        self.__STATE = {'leds': {}, 'params': {}}

    def led(
            self,
            led, brightness=None, speed=None, pulse=None, pulse_dir=None):

        # Make it list if it's not a list
        if isinstance(led, int):
            led = [led]

        # Light up the choosen LED
        self.set_leds(led, brightness, speed, pulse, pulse_dir).update_leds()

    def color(
            self,
            color, brightness=None, speed=None, pulse=None, pulse_dir=None):

        leds = ()

        # Check if an available color is choosen
        if color in COLOR_LIST:
                leds = COLOR_LED_LIST[color - 1]
        elif color in COLOR_NAME_LIST:
                leds = COLOR_LED_LIST[COLOR_NAME_LIST.index(color)]
        else:
            raise PyGlowException(
                self, "Invalid color: %s. Color must be a number from 1 to 6 "
                "or a name (%s)." % (color, ', '.join(COLOR_NAME_LIST)))

        # Light up the choosen LEDs
        self.set_leds(leds, brightness, speed, pulse, pulse_dir).update_leds()

    def arm(
            self,
            arm, brightness=None, speed=None, pulse=None, pulse_dir=None):

        leds = ()

        # Check if an existing arm is choosen
        if arm in ARM_LIST:
            leds = ARM_LED_LIST[arm - 1]
        else:
            raise PyGlowException(
                self, "Invalid arm number: %s. Arm must be a number from 1 to "
                "3." % (arm))

        # Light up the choosen LEDs
        self.set_leds(leds, brightness, speed, pulse, pulse_dir).update_leds()

    def all(self, brightness=None, speed=None, pulse=None, pulse_dir=None):
        # Light up all LEDs
        self.set_leds(
            LED_LIST, brightness, speed, pulse, pulse_dir).update_leds()

    def set_leds(
            self,
            leds, brightness=None, speed=None, pulse=None, pulse_dir=None):

        p = self.__STATE['params']

        # Store parameters value
        if brightness is not None:
            p['brightness'] = brightness
        else:
            brightness = self.brightness
        if speed is not None:
            p['speed'] = speed
        if pulse is not None:
            p['pulse'] = pulse
        if pulse_dir is not None:
            p['pulse_dir'] = pulse_dir

        # Check brightness value
        if not 0 <= brightness <= 255:
            raise PyGlowException(
                self, "Invalid brightness level: %s. Brightness level must be "
                "a number from 0 to 255." % (brightness))

        # Pick the gamma-corrected value
        gc_value = GAMMA_TABLE[brightness]

        for led in leds:
            m = re.match('^([a-z]+)([1-3])$', str(led))

            if m:
                color = m.group(1)
                arm = int(m.group(2))
                color_index = None

                # Check if the color has a valid name
                if color in COLOR_NAME_LIST:
                    color_index = COLOR_NAME_LIST.index(color)
                else:
                    raise PyGlowException(
                        self,
                        "Invalid color name: %s. Color name must be one of "
                        "the following: %s." %
                        (color, ', '.join(COLOR_NAME_LIST)))

                # Check if the arm has a valid number
                if arm in ARM_LIST:
                    led = LED_HEX_LIST[6 * (arm - 1) + 5 - color_index]
                else:
                    raise PyGlowException(
                        self, "Invalid arm number: %s. Arm must be a number "
                        "from 1 to 3." % (arm))
            elif (
                    isinstance(led, int) and
                    1 <= led <= 18):

                led = LED_HEX_LIST[led - 1]
            else:
                raise PyGlowException(
                    self, "Invalid LED number %s. LED must be a number from 1 "
                    "to 18." % (led))

            # Store the LED and brightness value
            self.__STATE['leds'][led] = gc_value

        return self

    def update_leds(self):
        p = self.__STATE['params']

        # Set default parameters value
        if 'brightness' not in p or p['brightness'] is None:
            p['brightness'] = self.brightness
        if 'speed' not in p or p['speed'] is None:
            p['speed'] = self.speed
        if 'pulse' not in p or p['pulse'] is None:
            p['pulse'] = self.pulse
        if 'pulse_dir' not in p or p['pulse_dir'] is None:
            p['pulse_dir'] = self.pulse_dir

        # Decide whether to pulse or just to light up
        if p['brightness'] > 0 and p['pulse']:
            self.__pulse(
                self.__STATE['leds'].keys(),
                p['brightness'], p['speed'], p['pulse_dir'])
        else:
            self.__write_data(self.__STATE['leds'].iteritems())

        # Reset the SET variable
        self.__STATE = {'leds': {}, 'params': {}}

    def __pulse(self, leds, brightness, speed, pulse_dir):
        # Check speed value
        if speed < 1:
            raise PyGlowException(
                self, "Invalid speed: %s. Speed must be a positive non-zero "
                "number." % (speed))

        # Choose pulsation style
        elif pulse_dir == UP:
            self.__pulse_loop(leds, 0, brightness, speed, UP)
        elif pulse_dir == DOWN:
            self.__pulse_loop(leds, brightness, 0, speed, DOWN)
        else:
            self.__pulse_loop(leds, 0, brightness, speed / 2, UP)
            self.__pulse_loop(leds, brightness, 0, speed / 2, DOWN)

    def __pulse_loop(self, leds, b_from, b_to, speed, direction):
        # Bigger from the pair
        b_max = float(max([b_from, b_to]))

        # Starting value
        b_val = float(b_from)

        # Maximum steps per second
        s_max = 20.0
        # Compensation constant
        # (the comp_const velue is a compensation of the delay of the other
        # commands in the loop - it's influenced by the s_max value)
        comp_const = 1030.0

        # Number of steps of the loop
        steps = speed / 1000.0 * s_max

        # Default increment value
        inc_val = b_max / steps

        # Step up the brightness
        for n in xrange(1, int(steps) + 1):
            # Calculate new brightness value
            b_val += inc_val * direction

            # Round the final brightness value to the desired value
            if n == int(steps) or b_val < 0:
                b_val = b_to

            # Set the brightness
            self.__write_data(
                tuple(
                    (n, GAMMA_TABLE[int(b_val)])
                    for n in self.__STATE['leds'].iterkeys()))

            # Sleep for certain period
            sleep(speed / steps / comp_const)

    def __write_data(self, leds):
        # Set LED brightness
        for led, brightness in leds:
            self.bus.write_byte_data(
                I2C_ADDR,
                int(led),
                brightness)

        # Light up all chosen LEDs
        self.bus.write_byte_data(I2C_ADDR, UPD_PWM_ADDR, 0xFF)


class PyGlowException(Exception):
    def __init__(self, parent, msg):
        # Switch all LEDs off
        parent.all(0)

        self.message = msg

    def __str__(self):
        return self.message
