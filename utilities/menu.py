from os.path import exists
from pick import pick
import pickle
from utilities.arena import Arena
from characters.character import Character
from characters.classe.archer import Archer
from characters.classe.barbarian import Barbarian
from characters.classe.mage import Mage
from characters.classe.tank import Tank
from armors.helmet import Helmet
from armors.chestplate import Chestplate
from armors.leggings import Leggings
from armors.boots import Boots
from weapons.arc import Arc
from weapons.baton import Baton
from weapons.bouclier import Bouclier
from weapons.hachette import Hachette
from weapons.masse import Masse
import gears.all_armors
import gears.all_weapons
import os


cls = lambda: os.system('cls')

Players = {}

def menu(title:str, options: list[str]):
    option, index = pick(options, title, indicator='->', default_index=0)
    return index

def submenu_play(title:str):
    global Players
    print(Players)
    Players.clear()
    if exists('Players.pkl'):
        with open('Players.pkl', 'rb') as file:
            # Call load method to deserialze
            Players = pickle.load(file)
    while True:
        choice = menu(title, ['Arena (Player)', 'Arena (Mob)', 'Quit'])
        match choice:
            case 0:
                print("Arena (Player)")
                cls()
                if len(Players) >= 2:
                    submenu_pre_fight_player(title)
                else:
                    Players[(len(Players) + 1)] = create_characters(title)
                    with open('Players.pkl', 'wb') as file: 
                        # A new file will be created
                        pickle.dump(Players, file)
            case 1:
                print("Arena (Mob)")
                if len(Players) > 0:
                    pass
                else:
                    pass
                cls()
            case 2:
                break

def submenu_pre_fight_player(title:str):
    global Players
    Players.clear()
    if exists('Players.pkl'):
        with open('Players.pkl', 'rb') as file:
            # Call load method to deserialze
            Players = pickle.load(file)
    list = []
    for cle, valeur in Players.items():
        list.append(valeur.name)
    while True:
        choice = menu("Choisir votre personnage:", list)
        Player1 = getCharactereByName(list[choice], Players)
        list.pop(choice)
        choice = menu("Choisir votre adversaire:", list)
        Player2 = getCharactereByName(list[choice], Players)
        Arena.fight(Player1, Player2)
        break

def create_characters(title:str) -> Character:
    name = input("Sasir le nom de votre héros: ")
    choice = menu(title, ['Archer', 'Barbarian', 'Mage', 'Tank'])
    match choice:
            case 0:
                p = Archer(name)
                p.set_helmet(choose_armor_helmet("Choisir votre casque"))
                p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
                p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
                p.set_boots(choose_armor_boots("Choisir vos chaussure"))
                p.set_weapon(choose_weapon_bow("Choisir ton arc"))
                p.full_heal()
                return p
            case 1:
                p = Barbarian(name)
                p.set_helmet(choose_armor_helmet("Choisir votre casque"))
                p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
                p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
                p.set_boots(choose_armor_boots("Choisir vos chaussure"))
                p.set_weapon(choose_weapon_hatchet("Choisir ta hachette"))
                p.full_heal()
                return p
            case 2:
                p = Mage(name)
                p.set_helmet(choose_armor_helmet("Choisir votre casque"))
                p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
                p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
                p.set_boots(choose_armor_boots("Choisir vos chaussure"))
                p.set_weapon(choose_weapon_staff("Choisir vos baton"))
                p.full_heal()
                return p
            case 3:
                p = Tank(name)
                p.set_helmet(choose_armor_helmet("Choisir votre casque"))
                p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
                p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
                p.set_boots(choose_armor_boots("Choisir vos chaussure"))
                p.set_weapon(choose_weapon_mass("Choisir votre masse"))
                p.set_shield(choose_weapon_shield("Choisir votre bouclier"))
                p.full_heal()
                return p

def choose_armor_helmet(title:str) -> Helmet:
    choice = menu(title, gears.all_armors.get_all_name_helmet_start())
    return gears.all_armors.starter_helmets[choice]

def choose_armor_chestplate(title:str) -> Chestplate:
    choice = menu(title, gears.all_armors.get_all_name_chestplate_start())
    return gears.all_armors.starter_chestplate[choice]

def choose_armor_leggins(title:str) -> Leggings:
    choice = menu(title, gears.all_armors.get_all_name_leggins_start())
    return gears.all_armors.starter_leggings[choice]

def choose_armor_boots(title:str) -> Boots:
    choice = menu(title, gears.all_armors.get_all_name_boots_start())
    return gears.all_armors.starter_boots[choice]

def choose_weapon_bow(title:str) -> Arc:
    choice = menu(title, gears.all_weapons.get_all_name_bow_start())
    return gears.all_weapons.starter_bow[choice]

def choose_weapon_staff(title:str) -> Baton:
    choice = menu(title, gears.all_weapons.get_all_name_staff_start())
    return gears.all_weapons.starter_staff[choice]

def choose_weapon_shield(title:str) -> Bouclier:
    choice = menu(title, gears.all_weapons.get_all_name_shield_start())
    return gears.all_weapons.starter_shield[choice]

def choose_weapon_hatchet(title:str) -> Hachette:
    choice = menu(title, gears.all_weapons.get_all_name_hatchet_start())
    return gears.all_weapons.starter_hatchet[choice]

def choose_weapon_mass(title:str) -> Masse:
    choice = menu(title, gears.all_weapons.get_all_name_mass_start())
    return gears.all_weapons.starter_mass[choice]

def getCharactereByName(name:str, Players:dict) -> Character:
    for cle, valeur in Players.items():
        if valeur.name == name:
            return valeur