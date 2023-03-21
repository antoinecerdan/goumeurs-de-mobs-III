class Arena:
    def __init__(self) -> None:
        pass

    def fight(first_character,second_character):
        print(first_character)
        print(second_character)
        while not (first_character.is_dead() or second_character.is_dead()):
            dmg = first_character.has_crit(first_character.choose_attack()) 
            dmg = first_character.damage_reduction(dmg,second_character)
            first_character.attack(dmg, second_character)
            print(f"{first_character.name} attacked {second_character.name} and he made {dmg} damages")
            if not second_character.is_dead():
                dmg = second_character.has_crit(second_character.choose_attack()) 
                dmg = second_character.damage_reduction(dmg,first_character)
                second_character.attack(dmg, first_character)
                print(f"{second_character.name} attacked {first_character.name} and he made {dmg} damages")
            print(first_character)
            print(second_character)
        if first_character.is_dead():
            print(f"{second_character.name} winning the fight")
            player_won = False
        else:
            print(f"{first_character.name} winning the fight")
            player_won = True
        first_character.full_heal()
        second_character.full_heal()