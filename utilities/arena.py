class Arena:
    def __init__(self) -> None:
        pass

    def fight(first_character,second_character):
        print(first_character)
        print(second_character)
        while not (first_character.is_dead() or second_character.is_dead()):
            xd = first_character.choose_attack()
            print(xd)
        
        if first_character.is_dead():
            player_won = False
        else:
            player_won = True
        first_character.choose_attack()