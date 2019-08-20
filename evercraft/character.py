from enum import Enum

class Alignment(Enum):
    Good = 1
    Neutral = 2
    Evil = 3


class Character:
    
    def __init__(self, name: str, alignment: Alignment = Alignment.Good):
        self.name = name
        self.alignment = alignment
        self.armor_class = 10
        self.hit_points = 5
        self.strength = 10
        self.wisdom = 10
        self.intelligence = 10
        self.dexterity = 10
        self.constitution = 10
        self.charisma = 10

    def isdead(self) -> bool:
        
        return self.hit_points < 1
