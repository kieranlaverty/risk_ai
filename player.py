"""
This class holds the players and the infomation of the players
"""

class player():

    def __init__(self, color = "rainbow", ai = True) -> None:
        self.color = color
        self.cards = []
        self.is_ai = ai


