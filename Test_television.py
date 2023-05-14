# Ella Lureen C. Calugay | Assignment 6 | UML Class Diagram

import pygame
from Television import TV

# Pseudo code
# Create TV 1
television1 = TV()
# Turn on TV 1
television1.turn_on()
# Set the channel of TV 1 to 30
television1.set_channel(30)
# Set the volume of tv 1 to 3
television1.set_volume(3)
# Print the TV 1 status
print("tv1's channel is",television1.get_channel(),"and volume level is",television1.get_volume())

# Create TV 2
television2 = TV()
# Turn on TV 2
television2.turn_on()
# Set the channel of TV 2 to 3
television2.set_channel(3)
# Set the volume of TV 2 to 2
television2.set_volume(2)
# Print the TV 2 status
print("tv2's channel is",television2.get_channel(),"and volume level is",television2.get_volume())