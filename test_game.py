import rock_paper_scissors as game

def test_user_choice():
    assert game.is_valid_choice("rock") == True
    assert game.is_valid_choice("paper") == True
    assert game.is_valid_choice("scissors") == True
    assert game.is_valid_choice("invalid") == False
