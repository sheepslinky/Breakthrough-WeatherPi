#!/usr/bin/env python3


###   load the modules

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

### Define variables and values

# colors
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (159, 0, 255)
blk = (0, 0, 0)  # blk stands for empty/black

#messages

message = "Hello Color"
message2 = "wow"
speed = 0.05


# Main Program

print('hello world')

#letters

sense.show_letter("O", yellow, back_colour=blue)
sleep(1)
sense.show_letter("M", blue, back_colour=red)
sleep(1)
sense.show_letter("G", green, back_colour=indigo)
sleep(1)
sense.show_letter("!", orange, back_colour=violet)
sleep(1)

#message
sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
sense.show_message(message2, speed, text_colour=yellow, back_colour=blue)

#clear the screen
sense.clear()

