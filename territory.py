"""
This class will hold the territories that make up the board
"""

class territory():

    def __init__(self, name = "Luthidel", troops = 0, color = None) -> None:
        self.name = name
        self.troops = troops
        self.color = color
        self.value = 0