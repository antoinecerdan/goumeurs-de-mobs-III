class Arena:
    def __init__(self) -> None:
        pass
    
    def fight_PvP(first_character, second_character):
        # Boucle de combat jusqu'à ce qu'un personnage meurt
        while not (first_character.is_dead() or second_character.is_dead()):
            # Détermination des dégâts infligés par le premier personnage
            dmg = first_character.damage_reduction(first_character.has_crit(first_character.choose_attack()),second_character)
            first_character.attack(dmg, second_character)
            # Si le deuxième personnage n'est pas mort, détermination des dégâts infligés par le deuxième personnage
            if not second_character.is_dead():
                dmg = second_character.damage_reduction(second_character.has_crit(second_character.choose_attack()),first_character)
                second_character.attack(dmg, first_character)
            # Affichage des informations des deux personnages après chaque tour de combat
            print(first_character)
            print(second_character)
        # Affichage du nom du personnage gagnant
        if first_character.is_dead():
            input(f"{second_character.name} winning the fight. Press ENTER to exit the PVP arene mode")
        else:
            input(f"{first_character.name} winning the fight. Press ENTER to exit the PVP arene mode")
        # Récupération de tous les points de vie pour les deux personnages
        first_character.full_heal()
        second_character.full_heal()
        first_character.full_mana_rage()
        second_character.full_mana_rage()
    
    def fight_PvE(first_character, second_character):
        # Boucle de combat jusqu'à ce qu'un personnage meurt
        while not (first_character.is_dead() or second_character.is_dead()):
            # Détermination des dégâts infligés par le premier personnage
            dmg = first_character.damage_reduction(first_character.has_crit(first_character.choose_attack()),second_character)
            first_character.attack(dmg, second_character)
            # Si le deuxième personnage n'est pas mort, détermination des dégâts infligés par le deuxième personnage
            if not second_character.is_dead():
                dmg = second_character.damage_reduction(second_character.has_crit(second_character.choose_attack()),first_character)
                second_character.attack(dmg, first_character)
            # Affichage des informations des deux personnages après chaque tour de combat
            print(first_character)
            print(second_character)
        # Affichage du nom du personnage gagnant
        if first_character.is_dead():
            input(f"{second_character.name} won the fight. Press ENTER to exit the PVE arene mode")
        else:
            input(f"{first_character.name} won the fight. Press ENTER to exit the PVE arene mode")
        # Récupération de tous les points de vie pour les deux personnages
        first_character.full_heal()
        first_character.full_mana_rage()
