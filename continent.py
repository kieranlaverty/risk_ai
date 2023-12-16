"""
This class will hold a group of territories 
and will grant the player a continent bonus if
the player holds all territories in the group
"""

class continent():

    def __init__(self, bonus = 2, name = "roshar") -> None:
        self.bonus = bonus
        self.name = name 
