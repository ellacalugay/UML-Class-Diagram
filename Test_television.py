# Ella Lureen C. Calugay | Assignment 6 | UML Class Diagram

import pygame
from Television import TV

# Initialize Pygame
pygame.init()

# Set up the Pygame window
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TV Status")

# Pseudo code
# Create TV 1
television1 = TV()
# Turn on TV 1
television1.turn_on()
# Set the channel of TV 1 to 30
television1.set_channel(30)
# Set the volume of tv 1 to 3
television1.set_volume(3)

# Create TV 2
television2 = TV()
# Turn on TV 2
television2.turn_on()
# Set the channel of TV 2 to 3
television2.set_channel(3)
# Set the volume of TV 2 to 2
television2.set_volume(2)

# Set up font for text rendering
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render the TV status text
    text1 = font.render("tv1's channel is " + str(television1.get_channel()) + " and volume level is " + str(television1.get_volume()), True, (0, 0, 0))
    text2 = font.render("tv2's channel is " + str(television2.get_channel()) + " and volume level is " + str(television2.get_volume()), True, (0, 0, 0))
    
    # Place the text in the center of the screen.
    text1_rect = text1.get_rect(center=(width/2, height/2 - 20))
    text2_rect = text2.get_rect(center=(width/2, height/2 + 20))

    # Display the text onto the screen
    screen.fill((255, 182, 193))
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)

    # Update the screen
    pygame.display.flip()