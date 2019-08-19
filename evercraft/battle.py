from evercraft.character import Character

def attack(roll: int, defender: Character) -> bool:
    return roll > defender.armor_class