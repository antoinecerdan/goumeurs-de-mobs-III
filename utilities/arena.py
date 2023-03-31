from sty import fg

class Arena:
    def __init__(self) -> None:
        pass
    
    def fight_PvP(first_character, second_character):
        # Boucle de combat jusqu'à ce qu'un personnage meurt
        while not (first_character.is_dead() or second_character.is_dead()):
            # Détermination des dégâts infligés par le premier personnage
            dmg = first_character.damage_reduction(first_character.has_crit(first_character.choose_attack()),second_character)
            first_character.attack(dmg, second_character)
            text = f"{first_character.name}"
            if first_character.hp:
                text += f"  {fg.red}{first_character.hp}{fg.rs}/{fg.red}{first_character.get_max_hp()} hp{fg.rs}"
            if hasattr(first_character, "mana"):
                text += f"  {fg.blue}{first_character.mana} mana{fg.rs}"
            if hasattr(first_character, "rage"):
                text += f"  {fg.yellow}{first_character.rage} rage{fg.rs}"
            print(text)
            text = f"{second_character.name}"
            if second_character.hp:
                text += f"  {fg.red}{second_character.hp}{fg.rs}/{fg.red}{second_character.get_max_hp()} hp{fg.rs}"
            if hasattr(second_character, "mana"):
                text += f"  {fg.blue}{second_character.mana} mana{fg.rs}"
            if hasattr(second_character, "rage"):
                text += f"  {fg.yellow}{second_character.rage} rage{fg.rs}"
            print(text)
            # Si le deuxième personnage n'est pas mort, détermination des dégâts infligés par le deuxième personnage
            if not second_character.is_dead():
                dmg = second_character.damage_reduction(second_character.has_crit(second_character.choose_attack()),first_character)
                second_character.attack(dmg, first_character)
                text = f"{first_character.name}"
                if first_character.hp:
                    text += f"  {fg.red}{first_character.hp}{fg.rs}/{fg.red}{first_character.get_max_hp()} hp{fg.rs}"
                if hasattr(first_character, "mana"):
                    text += f"  {fg.blue}{first_character.mana} mana{fg.rs}"
                if hasattr(first_character, "rage"):
                    text += f"  {fg.yellow}{first_character.rage} rage{fg.rs}"
                print(text)
                text = f"{second_character.name}"
                if second_character.hp:
                    text += f"  {fg.red}{second_character.hp}{fg.rs}/{fg.red}{second_character.get_max_hp()} hp{fg.rs}"
                if hasattr(second_character, "mana"):
                    text += f"  {fg.blue}{second_character.mana} mana{fg.rs}"
                if hasattr(second_character, "rage"):
                    text += f"  {fg.yellow}{second_character.rage} rage{fg.rs}"
                print(text)
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
            text = f"{first_character.name}"
            if first_character.hp:
                text += f"  {fg.red}{first_character.hp}{fg.rs}/{fg.red}{first_character.get_max_hp()} hp{fg.rs}"
            if hasattr(first_character, "mana"):
                text += f"  {fg.blue}{first_character.mana} mana{fg.rs}"
            if hasattr(first_character, "rage"):
                text += f"  {fg.yellow}{first_character.rage} rage{fg.rs}"
            print(text)
            text = f"{second_character.name}"
            if second_character.hp:
                text += f"  {fg.red}{second_character.hp}{fg.rs}/{fg.red}{second_character.get_max_hp()} hp{fg.rs}"
            print(text)
            # Si le deuxième personnage n'est pas mort, détermination des dégâts infligés par le deuxième personnage
            if not second_character.is_dead():
                dmg = second_character.damage_reduction(second_character.has_crit(second_character.choose_attack()),first_character)
                second_character.attack(dmg, first_character)
                # print les information du combats
                text = f"{first_character.name}"
                if first_character.hp:
                    text += f"  {fg.red}{first_character.hp}{fg.rs}/{fg.red}{first_character.get_max_hp()} hp{fg.rs}"
                if hasattr(first_character, "mana"):
                    text += f"  {fg.blue}{first_character.mana} mana{fg.rs}"
                if hasattr(first_character, "rage"):
                    text += f"  {fg.yellow}{first_character.rage} rage{fg.rs}"
                print(text)
                text = f"{second_character.name}"
                if second_character.hp:
                    text += f"  {fg.red}{second_character.hp}{fg.rs}/{fg.red}{second_character.get_max_hp()} hp{fg.rs}"
                print(text)
        # Affichage du nom du personnage gagnant
        if first_character.is_dead():
            input(f"{second_character.name} won the fight. Press ENTER to exit the PVE arene mode")
        else:
            input(f"{first_character.name} won the fight. Press ENTER to exit the PVE arene mode")
        # Récupération de tous les points de vie pour les deux personnages
        first_character.full_heal()
        first_character.full_mana_rage()
