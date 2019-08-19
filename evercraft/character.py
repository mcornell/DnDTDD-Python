from enum import Enum

class Alignment(Enum):
    Good = 1
    Neutral = 2
    Evil = 3


class Character:
    
    def __init__(self, name: str, alignment: Alignment = Alignment.Good):
        self.name = name
        self.alignment = alignment