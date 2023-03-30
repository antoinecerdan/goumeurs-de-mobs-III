import pyfiglet
from enum import Enum
import gears.all_armors,gears.all_tokens
from utilities.arena import Arena
import utilities.title
import utilities.menu
import random
from pick import pick
import sys
import pickle
import os
from os.path import exists

Players = {}

# Si le fichier Players.pkl existe, on le charge
if exists('Players.pkl'):
    with open('Players.pkl', 'rb') as file:
        Players = pickle.load(file) # Désérialise les données

# Efface l'écran
cls = lambda: os.system('cls')

# Choisit un titre au hasard
title = random.choice(utilities.title.title_choice)
# Utilise le titre pour créer un texte ASCII art avec la librairie Pyfiglet
figlet = pyfiglet.figlet_format("Goumeurs de mobs III", font = title[0], width = title[1])
# Concatène le titre et le texte ASCII art
title = f"{figlet} \n\n {title[2]} \n\n\n"

# Boucle principale du programme
while True:
    # Affiche le menu principal avec le titre
    choice = utilities.menu.menu(title, ['Play', 'New game', 'Quit'])
    
    # Utilise la structure switch/case pour gérer les choix de l'utilisateur
    match choice:
        case 0:
            print("Play")
            cls()
            # Si au moins un joueur existe, on affiche le sous-menu pour sélectionner un personnage
            if len(Players) >= 1:
                utilities.menu.submenu_play(title)
            # Sinon, on crée un nouveau joueur
            else:
                Players[(len(Players) + 1)] = utilities.menu.create_characters(title)
                with open('Players.pkl', 'wb') as file: 
                    pickle.dump(Players, file) # Sérialise les données et les enregistre dans le fichier 'Players.pkl'
        case 1:
            print("New game")
            if len(Players) > 0:
                pass # TODO: Gérer la création d'une nouvelle partie avec des joueurs existants
            else:
                pass # TODO: Gérer la création d'une nouvelle partie sans joueurs existants
            cls()
        case 2:
            # Sauvegarde les données des joueurs dans le fichier 'Players.pkl' avant de quitter le programme
            with open('Players.pkl', 'wb') as file: 
                pickle.dump(Players, file)
            cls() # Efface l'écran une dernière fois avant de quitter le programme
            break # Sort de la boucle principale et termine le programme


# GAME = False
# print("non")
# class State(Enum):
#     EXPLORE = 1
#     FIGHT = 2
#     TOWN = 3
#     DEAD = 4

# state = State.EXPLORE
# if state == state.EXPLORE:
#     print("yeysyyese")

# player = Archer("EosisWasTaken")
# player.set_helmet(gears.all_armors.get_random_gear(gears.all_armors.starter_helmets))
# player.set_chestplate(gears.all_armors.get_random_gear(gears.all_armors.starter_chestplate))
# player.set_leggings(gears.all_armors.get_random_gear(gears.all_armors.starter_leggings))
# player.set_boots(gears.all_armors.get_random_gear(gears.all_armors.starter_boots))
# player.set_token(gears.all_tokens.biden)
# player.set_token(gears.all_tokens.biden)
# player.set_token(gears.all_tokens.biden)
# player.print_tokens()
# player.full_heal()

# dummy =  Barbarian("eebhuyhnjkl")

# def menu():
#     menu_title = title
#     options = ['Play', 'Load', 'New game', 'Quit']

#     option, index = pick(options, menu_title, indicator='->', default_index=0)
#     return index

# choice = menu()
# match choice:
#         case 0:
#             print("Play")
#             GAME = True
#             cls()
#         case 1:
#             print("Load")
#             # Open the file in binary mode
#             with open('Players.pkl', 'rb') as file:
#                 # Call load method to deserialze
#                 Players = pickle.load(file)
#             cls()
#         case 2:
#             print("New game")
#             cls()
#         case 3:
#             cls()
#             # Open a file and use dump()
#             with open('Players.pkl', 'wb') as file: 
#             # A new file will be created
#                 pickle.dump(Players, file)
#             sys.exit()

# def sub_menu():
#     menu_title = title
#     options = ['Arena', 'Quit']

#     option, index = pick(options, menu_title, indicator='->', default_index=0)
#     return index

# def parse_user_input(cmd):
#         cmd.strip()
#         cmd.lower()
#         cmd = cmd.split()
#         print(cmd)
#         get_action(cmd)

# def get_action(cmd):
#         print(cmd)
#         match cmd[0]:
#                 case "say":
#                         say(cmd[1])
#                 case "arena":
#                         Arena.fight(player,dummy)

# def say(msg):
#     print(msg)

# while GAME:
#     choice = sub_menu()
#     match choice:
#         case 0:
#             cls()
#             Arena.fight(player,dummy)
#         case 1:
#             cls()
#             sys.exit()


