#!/usr/bin/env python3
### This is my computer program!! ###


### modules

from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (159, 0, 255)
blk = (0, 0, 0)  # blk stands for empty/black


message="H"
message2="a"
message3="p"
message4="p"
message5="y"
message6="B"
message7="d"
message8="a"
message9="y"


print('hello world')

#### rotation

sense.set_rotation(180)


### flash letters

sense.show_letter("Y", red)
sleep(.5)

sense.show_letter("O", red)
sleep(.5)

sense.show_letter("Y", red)
sleep(.5)

sense.show_letter("O", red)
sleep(.5)
sense.show_letter("Y", red)
sleep(.5)

sense.show_letter("O", red)
sleep(.5)
sense.show_letter("Y", red)
sleep(.5)

sense.show_letter("O", red)
sleep(.5)

#### scroll messages
sense.show_message(message, .03,text_colour=yellow, back_colour=blk)
sense.show_message(message2, .03,text_colour=blk, back_colour=blue)
sense.show_message(message3, .03,text_colour=violet, back_colour=yellow)
sense.show_message(message4, .03,text_colour=red, back_colour=blk)
sense.show_message(message5, .03,text_colour=red, back_colour=green)
sense.show_message(message6, .03,text_colour=orange, back_colour=blue)
sense.show_message(message7, .03,text_colour=blk, back_colour=indigo)
sense.show_message(message8, .03,text_colour=yellow, back_colour=blk)
sense.show_message(message9, .03,text_colour=blue, back_colour=indigo)

## clear the screeen

sense.clear()
