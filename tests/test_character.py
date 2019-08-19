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

    