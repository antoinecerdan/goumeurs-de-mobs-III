import pyfiglet
from enum import Enum
from characters.classe.archer import Archer
import gears.all_armors,gears.all_tokens
from utilities.arena import Arena
import random
from pick import pick
import sys
from os import system 

cls = lambda: system('cls')

title_choice = [
      ("big",210,"Better than the original game !"),
      ("colossal",150, "Vite fo goumer des mobs"),
      ("doom",150, "Et schlak !"),
      ("ivrit",100, "AAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
      ("rounded",100, "Better than Diablo IV !"),
      ("slant",120, "Very cool gaem 10/10")
]
title = random.choice(title_choice)
GAME = False
print("non")
class State(Enum):
    EXPLORE = 1
    FIGHT = 2
    TOWN = 3
    DEAD = 4

state = State.EXPLORE
if state == state.EXPLORE:
    print("yeysyyese")

figlet = pyfiglet.figlet_format("Goumeurs de mobs III", font = title[0], width = title[1])
title = f"{figlet} \n\n {title[2]} \n\n\n"

player = Archer("EosisWasTaken")
player.set_helmet(gears.all_armors.get_random_gear(gears.all_armors.starter_helmets))
player.set_chestplate(gears.all_armors.get_random_gear(gears.all_armors.starter_chestplate))
player.set_leggings(gears.all_armors.get_random_gear(gears.all_armors.starter_leggings))
player.set_boots(gears.all_armors.get_random_gear(gears.all_armors.starter_boots))
player.set_token(gears.all_tokens.biden)
player.set_token(gears.all_tokens.biden)
player.set_token(gears.all_tokens.biden)
player.print_tokens()

dummy =  Archer("eebhuyhnjkl")

print(player)

def menu():
    menu_title = title
    options = ['Play', 'Load', 'New game', 'Quit']

    option, index = pick(options, menu_title, indicator='->', default_index=0)
    return index

choice = menu()
match choice:
        case 0:
            print("Play")
            GAME = True
            cls()
        case 1:
            print("Load")
            cls()
        case 2:
            print("New game")
            cls()
        case 3:
            cls()
            sys.exit()
            
print(choice)
def get_user_input(msg):
    return str(input(msg + " >>> "))

def parse_user_input(cmd):
        cmd.strip()
        cmd.lower()
        cmd = cmd.split()
        print(cmd)
        get_action(cmd)

def get_action(cmd):
        print(cmd)
        match cmd[0]:
                case "say":
                        say(cmd[1])
                case "arena":
                        Arena.fight(player,dummy)


def generate_user_interface():
    pass

def say(msg):
    print(msg)

while GAME:
    generate_user_interface()
    cmd = get_user_input("Tu fais quoi wsh")
    parse_user_input(cmd)
