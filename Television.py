# Ella Lureen C. Calugay | Assignment 6 | UML Class Diagram

# Pseudocode
# Create a class named TV
class TV:
    # Create a non-parametrized constructor
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.switch_button = False

# List all the methods that are needed
    # Create a turn on method
    def turn_on(self):
        self.switch_button = True

    # Create a turn off method
    def turn_off(self):
        self.switch_button = False

    # Create a get channel method
    def get_channel(self):
        return self.channel
    
    # Create a set channel method
    def set_channel(self, channel):
        if self.switch_button >= 1 and channel <= 120:
             self.channel = channel

# End of code.