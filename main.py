import pyfiglet
from enum import Enum
from characters.classe.archer import Archer
import gears.all_armors,gears.all_tokens
from utilities.arena import Arena

GAME = True

class State(Enum):
    EXPLORE = 1
    FIGHT = 2
    TOWN = 3
    DEAD = 4

state = State.EXPLORE
if state == state.EXPLORE:
    print("yeysyyese")

print(pyfiglet.figlet_format("Goumeurs de mobs III", font = "3-d" ))

player = Archer("EosisWasTaken")
player.set_helmet(gears.all_armors.get_random_gear(gears.all_armors.starter_helmets))
player.set_chestplate(gears.all_armors.get_random_gear(gears.all_armors.starter_chestplate))
player.set_leggings(gears.all_armors.get_random_gear(gears.all_armors.starter_leggings))
player.set_boots(gears.all_armors.get_random_gear(gears.all_armors.starter_boots))

dummy =  Archer("eebhuyhnjkl")

print(player)

def get_user_input(msg):
    return str(input(msg + " >>>"))

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
