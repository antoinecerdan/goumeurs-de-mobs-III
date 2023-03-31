from os.path import exists
from pick import pick
import pickle
import random
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
from monsters.monster import Monster  # import de la classe Monster depuis le module monsters
import gears.all_armors
import gears.all_weapons
import gears.all_tokens
import os


# Fonction qui nettoie la console
cls = lambda: os.system('cls')

# Dictionnaire qui stocke les joueurs
Players = {}

# Fonction qui affiche un menu et retourne l'index de l'option choisie
def menu(title:str, options: list[str]):
    option, index = pick(options, title, indicator='->', default_index=0)
    return index

# Sous-menu pour la gestion des combats entre joueurs
def submenu_play(title:str):
    global Players
    # ça c'est juste que je suis parano
    Players.clear()
    # on vérifie si le fichier de sauvegarde existe avant de l'importer
    if exists('Players.pkl'):
        with open('Players.pkl', 'rb') as file:
            # Chargement des joueurs à partir du fichier binaire Players.pkl
            Players = pickle.load(file)
    while True:
        # Affichage du menu
        choice = menu(title, ['Arena (Player)', 'Arena (Mob)', 'Quit'])
        # Traitement du choix de l'utilisateur
        match choice:
            case 0:
                cls()
                #On vérifie si on possède bien 2 joueurs dans les données du jeu
                if len(Players) >= 2:
                    # Sous-menu pour la sélection des combattants
                    submenu_pre_fight_player()
                else:
                    #on crée un personnage pour PvP
                    Players[(len(Players) + 1)] = create_characters(title)
                    with open('Players.pkl', 'wb') as file: 
                        # Sauvegarde des joueurs dans le fichier binaire Players.pkl
                        pickle.dump(Players, file)
            case 1:
                if len(Players) >= 1:
                    submenu_pre_fight_mobs()
                else:
                    Players[(len(Players) + 1)] = create_characters(title)
                    with open('Players.pkl', 'wb') as file: 
                        # Sauvegarde des joueurs dans le fichier binaire Players.pkl
                        pickle.dump(Players, file)
            case 2:
                break

# Sous-menu pour la sélection des combattants
def submenu_pre_fight_player():
    global Players
    # ça c'est juste que je suis parano
    Players.clear()
    # on vérifie si le fichier de sauvegarde existe avant de l'importer
    if exists('Players.pkl'):
        with open('Players.pkl', 'rb') as file:
            # Chargement des joueurs à partir du fichier binaire Players.pkl
            Players = pickle.load(file)
    list = []
    # On va lister tout les joueurs possible afin de savoir qui affronté
    for cle, valeur in Players.items():
        list.append(valeur.name)
    while True:
        # Sélection du premier combattant
        choice = menu("Choisir votre personnage:", list)
        Player1 = getCharactereByName(list[choice], Players)
        # On retire le player 1 pour pas faire un 1vs1 contre soi même 
        list.pop(choice)
        # Sélection du second combattant
        choice = menu("Choisir votre adversaire:", list)
        Player2 = getCharactereByName(list[choice], Players)
        # Lancement du combat
        Arena.fight_PvP(Player1, Player2)
        break

def submenu_pre_fight_mobs():
    global Players
    # ça c'est juste que je suis parano
    Players.clear()
    # on vérifie si le fichier de sauvegarde existe avant de l'importer
    if exists('Players.pkl'):
        with open('Players.pkl', 'rb') as file:
            # Chargement des joueurs à partir du fichier binaire Players.pkl
            Players = pickle.load(file)
    list = []
    # On va lister tout les joueurs possible afin de savoir qui affronté
    for cle, valeur in Players.items():
        list.append(valeur.name)
    while True:
        # Sélection du premier combattant
        choice = menu("Choisir votre personnage:", list)
        Player1 = getCharactereByName(list[choice], Players)
        
        # Sélection du second combattant
        choice = menu("Choisir votre difficulté:", ["Niveau 1", "Niveau 2","Niveau 3","Niveau 4","Niveau 5"])
        # Lancement du combat
        Arena.fight_PvE(Player1, generate_one_mob(choice + 1))
        break

def create_characters(title:str) -> Character:
    # Demander le nom du héros
    name = input("Saisir le nom de votre héros: ")
    # Afficher le menu des choix de personnage
    choice = menu(title, ['Archer', 'Barbarian', 'Mage', 'Tank'])
    # Utiliser l'instruction "match" pour sélectionner la classe du personnage en fonction du choix
    match choice:
        # Si l'utilisateur a choisi "Archer"
        case 0:
            # Créer un objet Archer avec le nom du héros
            p = Archer(name)  
            # Choisir les différentes pièces d'armure et l'arme pour le personnage
            p.set_helmet(choose_armor_helmet("Choisir votre casque"))
            p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
            p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
            p.set_boots(choose_armor_boots("Choisir vos chaussure"))
            p.set_weapon(choose_weapon_bow("Choisir ton arc"))
            for x in gears.all_tokens.starter_magical_tokens_bow:
                p.set_token(x)
            # Restaurer la santé complète du personnage et le retourner
            p.full_heal()
            return p
        # Si l'utilisateur a choisi "Barbarian"
        case 1:
            # Créer un objet Barbarian avec le nom du héros
            p = Barbarian(name)
            # Choisir les différentes pièces d'armure et l'arme pour le personnage
            p.set_helmet(choose_armor_helmet("Choisir votre casque"))
            p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
            p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
            p.set_boots(choose_armor_boots("Choisir vos chaussure"))
            p.set_weapon(choose_weapon_hatchet("Choisir ta hachette"))
            for x in gears.all_tokens.starter_physical_tokens_hachette:
                p.set_token(x)
            # Restaurer la santé complète du personnage et le retourner
            p.full_heal()
            return p
        # Si l'utilisateur a choisi "Mage"
        case 2:
            # Créer un objet Mage avec le nom du héros
            p = Mage(name)
            # Choisir les différentes pièces d'armure et l'arme pour le personnage
            p.set_helmet(choose_armor_helmet("Choisir votre casque"))
            p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
            p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
            p.set_boots(choose_armor_boots("Choisir vos chaussure"))
            p.set_weapon(choose_weapon_staff("Choisir vos baton"))
            for x in gears.all_tokens.starter_magical_tokens_baton:
                p.set_token(x)
            # Restaurer la santé complète du personnage et le retourner
            p.full_heal()
            return p
        # Si l'utilisateur a choisi "Tank"
        case 3:
            # Créer un objet Mage avec le nom du héros
            p = Tank(name)
            # Choisir les différentes pièces d'armure et l'arme pour le personnage
            p.set_helmet(choose_armor_helmet("Choisir votre casque"))
            p.set_chestplate(choose_armor_chestplate("Choisir votre plastron"))
            p.set_leggings(choose_armor_leggins("Choisir votre pantalon"))
            p.set_boots(choose_armor_boots("Choisir vos chaussure"))
            p.set_weapon(choose_weapon_mass("Choisir votre masse"))
            p.set_shield(choose_weapon_shield("Choisir votre bouclier"))
            for x in gears.all_tokens.starter_physical_tokens_masse:
                p.set_token(x)
            # Restaurer la santé complète du personnage et le retourner
            p.full_heal()
            return p

def choose_armor_helmet(title:str) -> Helmet:
    # Affiche un menu pour sélectionner un casque et retourne le casque choisi
    choice = menu(title, gears.all_armors.get_all_name_helmet_start())
    return gears.all_armors.starter_helmets[choice]

def choose_armor_chestplate(title:str) -> Chestplate:
    # Affiche un menu pour sélectionner un plastron et retourne le plastron choisi
    choice = menu(title, gears.all_armors.get_all_name_chestplate_start())
    return gears.all_armors.starter_chestplate[choice]

def choose_armor_leggins(title:str) -> Leggings:
    # Affiche un menu pour sélectionner un pantalon et retourne le pantalon choisi
    choice = menu(title, gears.all_armors.get_all_name_leggins_start())
    return gears.all_armors.starter_leggings[choice]

def choose_armor_boots(title:str) -> Boots:
    # Affiche un menu pour sélectionner des bottes et retourne les bottes choisies
    choice = menu(title, gears.all_armors.get_all_name_boots_start())
    return gears.all_armors.starter_boots[choice]

def choose_weapon_bow(title:str) -> Arc:
    # Affiche un menu pour sélectionner un arc et retourne l'arc choisi
    choice = menu(title, gears.all_weapons.get_all_name_bow_start())
    return gears.all_weapons.starter_bow[choice]

def choose_weapon_staff(title:str) -> Baton:
    # Affiche un menu pour sélectionner un bâton et retourne le bâton choisi
    choice = menu(title, gears.all_weapons.get_all_name_staff_start())
    return gears.all_weapons.starter_staff[choice]

def choose_weapon_shield(title:str) -> Bouclier:
    # Affiche un menu pour sélectionner un bouclier et retourne le bouclier choisi
    choice = menu(title, gears.all_weapons.get_all_name_shield_start())
    return gears.all_weapons.starter_shield[choice]

def choose_weapon_hatchet(title:str) -> Hachette:
    # Affiche un menu pour sélectionner une hachette et retourne la hachette choisie
    choice = menu(title, gears.all_weapons.get_all_name_hatchet_start())
    return gears.all_weapons.starter_hatchet[choice]

def choose_weapon_mass(title:str) -> Masse:
    # Affiche un menu pour sélectionner une masse et retourne la masse choisie
    choice = menu(title, gears.all_weapons.get_all_name_mass_start())
    return gears.all_weapons.starter_mass[choice]

def getCharactereByName(name:str, Players:dict) -> Character:
    # Parcourt le dictionnaire "Players" pour trouver le personnage dont le nom correspond à "name", et retourne le personnage
    for cle, valeur in Players.items():
        if valeur.name == name:
            return valeur

def generate_one_mob(difficulty) -> Monster:
        """
        Génère un monstres en fonction de la difficulté donnée

        Parameters:
        difficulty (int): difficulté de la pièce
        """
        if difficulty <= 1:
            return Monster(random.randrange(1,10*difficulty),Monster.get_random_name())
        if difficulty == 2:
            return Monster(random.randrange(10,10*difficulty),Monster.get_random_name())
        if difficulty == 3:
            return Monster(random.randrange(20,10*difficulty),Monster.get_random_name())
        if difficulty == 4:
            return Monster(random.randrange(30,10*difficulty),Monster.get_random_name())
        if difficulty >= 5:
            return Monster(random.randrange(40,10*difficulty),Monster.get_random_name())
