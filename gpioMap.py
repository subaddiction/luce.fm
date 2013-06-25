#Fourierizer
#A real-time sound analysis engine to extract frequency bands values from audio signal
# FOR NOW, THIS IS PSEUDO-CODE

#Mathematical functions
import numpy
import scipy

#GPIO driver - basic
#import RPi.GPIO as GPIO
#setup gpio numbering mode
#GPIO.setmode(GPIO.BOARD)

#GPIO driver - advanced
#import RPIO as RPIO

from RPIO import PWM

# Setup PWM and DMA channel 0
PWM.setup()
PWM.init_channel(0)

# Add some pulses to the subcycle
PWM.add_channel_pulse(0, 17, 0, 50)
PWM.add_channel_pulse(0, 17, 100, 50)

# Stop PWM for specific GPIO on channel 0
PWM.clear_channel_gpio(0, 17)

# Shutdown all PWM and DMA activity
PWM.cleanup()




###BOF TEST

###setup pin directions
##GPIO.setup(11, GPIO.OUT)
##GPIO.setup(12, GPIO.OUT)
##
###output signal to pin
##GPIO.output(11, GPIO.LOW)
##GPIO.output(12, GPIO.HIGH)
##
##print(GPIO.input(11))
##print(GPIO.input(12))


# EXAMPLE FROM INTERNET
### use P1 header pin numbering convention
##GPIO.setmode(GPIO.BOARD)
##
### Set up the GPIO channels - one input and one output
##GPIO.setup(11, GPIO.IN)
##GPIO.setup(12, GPIO.OUT)
##
### Input from pin 11
##input_value = GPIO.input(11)
##
### Output to pin 12
##GPIO.output(12, GPIO.HIGH)
##
### The same script as above but using BCM GPIO 00..nn numbers
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(17, GPIO.IN)
##GPIO.setup(18, GPIO.OUT)
##input_value = GPIO.input(17)
##GPIO.output(18, GPIO.HIGH)

###EOF TEST

## GPIO SAMPLE MAPPING
## gh0 > gpio0 > R1 & B3
## gh1 > gpio1 > G1
## gh2 > gpio2 > B1
##
## gh1 > gpio3 > R2
## gh0 > gpio4 > G2
## gh2 > gpio5 > B2
##
## gh2 > gpio6 > R3
## gh1 > gpio7 > G3
##
## +----------------+
## |      COL3      |
## |  +----------+  |
## |  |   COL2   |  |
## |  |  +----+  |  |
## |  |  |COL1|  |  |
## |  |  +----+  |  |
## |  |          |  |
## |  +----------+  |
## |                |
## +----------------+
##

## SIMPLIFY...
## gh0 > gpio0 > R1 B3 G2
## gh1 > gpio1 > G1 R2 G3
## gh2 > gpio2 > B1 B2 R3






