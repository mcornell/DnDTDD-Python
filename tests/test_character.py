from evercraft.character import Character, Alignment

def test_character_can_be_created():
    
    character = Character("Tom")

    assert character.name == "Tom"

def test_character_can_change_their_name():
    
    character = Character("Tom")

    character.name = "Michael"
    assert character.name == "Michael"

def test_character_can_be_created_with_alignment():
    
    character = Character("Jared", Alignment.Evil)

    assert character.alignment == Alignment.Evil


def test_character_can_change_alignment():
    
    character = Character("Jared", Alignment.Evil)
    character.alignment = Alignment.Neutral
    assert character.alignment == Alignment.Neutral

def test_character_is_good_by_default():
    character = Character("Tom")
    assert character.alignment == Alignment.Good


def test_character_has_default_armor_class():
    character = Character("Jared")
    assert character.armor_class == 10


def test_character_has_five_hit_points_to_start():
    character = Character("Jared")

    assert character.hit_points == 5    



