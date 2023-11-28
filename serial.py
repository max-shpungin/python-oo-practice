class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    # needs to store the number starting with 100
    # when called the number needs to increase by 1
    # when reset() the number needs to reset to 100

    def __init__(self,start):
        """sets the starting value to start"""
        self.previous_value = self.initial_counter_value = start - 1 #probably should be a diff name e.g. previous
        #self.starting_value = start - 1#probably should be a diff name

    def generate(self):
        """increment the current value by one"""
        self.previous_value += 1
        return self.previous_value

    def reset(self):
        """resets the current value back to the starting value"""
        self.previous_value = self.initial_counter_value
