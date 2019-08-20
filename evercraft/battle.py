from evercraft.character import Character

def attack(roll: int, defender: Character) -> bool:
    if roll > defender.armor_class:
        damage = 1
        if roll == 20:
            damage = damage * 2
        defender.hit_points -= damage
        return True
    return False