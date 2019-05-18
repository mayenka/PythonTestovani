import rock_paper_scissors

def test_rock_rock_is_tie():
    '''testuje, že dva stejné výstupy jsou remíza'''
    assert rock_paper_scissors.determine_game_result('rock', 'rock') == 'tie'

def test_random_play_is_always_valid():
    for _ in range(10000):
        assert rock_paper_scissors.is_valid_play(rock_paper_scissors.random_play())
    #nepotřebuji is True, protože jen ověřuji, že tah je správný
    #otestuji jen to, že při jednom tahu je vše v pořádu, ale netestuje, co se stane,
    #když je více tahů

def test_random_play_is_fair():
    '''test, že funkce hraje náhodně a fair'''
    plays = {
    'rock': 0,
    'paper' : 0,
    'scissors' : 0
    }
    for _ in range(10000):      #podtržítko nahrazuje jméno proměnnou, použít jen, když už nebudu potřebovat
    #nikde jinde použít
        play = rock_paper_scissors.random_play()
        plays[play] += 1

    for value in plays.values():
        assert value > 3000

def test_rock_is_valid_play():       #u testu je dobré mít název co nejvíce popisný
    assert rock_paper_scissors.is_valid_play('rock') is True
    # is znamená 'je to ta samá věc', ověřuji, že ta věc vrátila True, nejen to, že je to True

def test_paper_is_valid_play():
    assert rock_paper_scissors.is_valid_play('paper') is True

def test_scissors_is_valid_play():       #u testu je dobré mít název co nejvíce popisný
    assert rock_paper_scissors.is_valid_play('scissors') is True

def test_spock_is_not_valid_play():
    assert rock_paper_scissors.is_valid_play('spock') is False

def test_lizzard_is_not_valid_play():
    assert rock_paper_scissors.is_valid_play('lizzard') is False
