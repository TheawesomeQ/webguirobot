# # We're starting with basic PWM output and seeing what we can do.
# # This is using the i2c pwm output.

# # https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16-channel-servo-driver-with-raspberry-pi.pdf

# # We're using this library; the adafruit-pca9685 is deprecated in favor of adafruit-circuitpython-pca9685
# # https://github.com/adafruit/Adafruit_CircuitPython_PCA9685

import board
import time

from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution. I.e. only the first three chars represent functional bits
level = 0x000F
while(True):
    while(level < 0xFFFF):
        pca.channels[0].duty_cycle = level
        level = level + 0x0100
        time.sleep(0.01)
    while(level > 0x0000):
        pca.channels[0].duty_cycle = level
        level = level - 0x0100
        time.sleep(0.01)

# import time
# from adafruit_servokit import ServoKit
# kit = ServoKit(channels=8)
# kit.servo[0].angle=180