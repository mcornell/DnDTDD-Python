from evercraft.character import Character
from evercraft import battle

def test_character_must_beat_armor_class_to_hit_opponent():
    attacker = Character("Jared")
    defender = Character("Robert")

    roll = 11
    assert battle.attack(roll, defender)