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

    def isdead(self) -> bool:
        
        return self.hit_points < 1
