class Arena:
    def __init__(self) -> None:
        pass

    def fight(first_character,second_character):
        while not (first_character.is_dead() or second_character.is_dead()):
            dmg = first_character.damage_reduction(first_character.has_crit(first_character.choose_attack()),second_character)
            first_character.attack(dmg, second_character)
            if not second_character.is_dead():
                dmg = second_character.damage_reduction(second_character.has_crit(second_character.choose_attack()),first_character)
                second_character.attack(dmg, first_character)
            print(first_character)
            print(second_character)
        if first_character.is_dead():
            input(f"{second_character.name} winning the fight. Press ENTER to exit the PVP arene mode")
        else:
            input(f"{first_character.name} winning the fight. Press ENTER to exit the PVP arene mode")
        first_character.full_heal()
        second_character.full_heal()