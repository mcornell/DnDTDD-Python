from evercraft.character import Character
from evercraft import battle

def test_character_must_beat_armor_class_to_hit_opponent():
    attacker = Character("Jared")
    defender = Character("Robert")

    roll = 11
    assert battle.attack(roll, defender)

def test_character_must_beat_armor_class_to_hit_opponent():
    attacker = Character("Jared")
    defender = Character("Robert")

    roll = 10
    assert battle.attack(roll, defender) == False

def test_when_attack_is_successful_the_defender_takes_1_point_of_damage():
    attacker = Character("Jared")
    defender = Character("Robert")

    roll = 11
    battle.attack(roll, defender)
    assert defender.hit_points == 4


def test_when_attack_is_a_natural_20_the_damage_is_doubled():
    attacker = Character("Jared")
    defender = Character("Robert")

    roll = 20
    battle.attack(roll, defender)
    assert defender.hit_points == 3