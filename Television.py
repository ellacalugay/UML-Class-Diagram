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
        if self.channel >= 1 and channel <= 120:
             self.channel = channel

    # Create a get volume method
    def get_volume(self):
        return self.volume_level

    # Create a set volume method
    def set_volume(self, volume_level):
        if self.volume_level >= 1 and volume_level <= 7:
            self.volume_level = volume_level

    # Create a channel up method
    def channel_up(self):
        if self.channel < 120:
            self.channel += 1
        else:
            self.channel=1     

    # Create a channel down method   
    def channel_down(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120

    # Create a volume up method
    def volume_up(self):
        if self.channel < 7:
            self.channel += 1
        else:
            self.channel = 1

    # Create a volume down method
    def volume_down(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 7

# End of code.