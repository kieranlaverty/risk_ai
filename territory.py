"""
This class will hold the territories that make up the board
"""

class territory():

    def __init__(self, name = "Luthidel", links = []) -> None:
        self.name = name
        self.links = links
        self.value = 0