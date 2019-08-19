from evercraft.character import Character

def test_character_can_be_created():
    
    character = Character("Tom")

    assert character.name == "Tom"

def test_character_can_change_their_name():
    
    character = Character("Tom")

    character.name = "Michael"
    assert character.name == "Michael"