import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Character Setup ####
class character:
    def __init__(self):
        self.alive = True
        self.name = ''
        self.race = ''
        self.clas = ''
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.quest = ""
        self.object = ""
        self.location = 'b2'
character = character()

class item:
    def __init__(self):
        self.item1 = 'SWORD'
        self.item2 = 'POTION'
        self.item3 = 'ARMOR'
        self.item4 = 'GOLD COIN'
item = item()

class loot:
    def __init__(self):
        self.got_loot = 0
        self.what_loot = 0
        self.got_loot = random.randint(1,2)
        self.equip = ""
        
    def loot_won(self):
        if self.got_loot == 1:
            print("You got loot for winning the battle,")
            self.what_loot = random.randint(1,3)
            if self.what_loot == 1:
                print("You received their weapon parts")
                inventory.inv.append("WEAPON PARTS")
                self.equip = str(input("Do you want to equip what you got, if you do not enter yes you wont equip the item"))
                if self.equip.lower() == "yes":
                    character.attack += 5
            elif self.what_loot == 2:
                print("You received their armor parts")
                inventory.inv.append("ARMOR PARTS")
                self.equip = str(input("Do you want to equip what you got, if you do not enter yes you wont equip the item"))
                if self.equip.lower() == "yes":
                    character.defense += 2
                    print("You equiped the parts")
            elif self.what_loot == 3:
                print("You received a potion that heals you, +30 to health")
                character.hp += 30
        elif self.got_loot == 2:
            print("You didn't get any loot from the enemy")
loot = loot()
    
class inventory():
    def __init__(self):
        self.inv = []      
inventory = inventory()

class enemy():
    def __init__(self):
        self.name = ''
        self.alive = True
        self.hp = 0
        self.attack = 0
        self.defense = 0
enemy = enemy()

#### Tile Screen ####
def title_scr_options():
    option = ("")
    while option.lower() not in ['play', 'help', 'exit']:
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("assistance"):
            help_menu()
        elif option.lower() == ("exit"):
            sys.exit()
        else:
            print("Enter a correct input!")
                 
def title_screen():
    os.system('cls')
    print("##########################MAIN MENU#########################")
    print("############***#########***######***#########***############")
    print("###########***#######***############***#######***###########")
    print("##########***----------------------------------***##########")
    print("#########***#####----Welcome To Aincrad----#####***#########")
    print("########***--------------------------------------***########")
    print("_______#***#####***---------play---------***#####***#_______")
    print("_____#***######***-------assistance-------***######***#_____")
    print("_______#***-----------------exit-----------------***#_______")
    print("_______#***--------------------------------------***#_______")
    print("_______#******Recomended to study the help menu*****#_______")
    print("#########***-------------------------------------***########")
    print("##########***#######***###############***#######***#########")
    print("############***#######***#Main Menu#***########***##########")
    title_scr_options()

def help_menu():
    os.system('cls')
    print("##########################HELP MENU#########################")
    print("##########################?????????#########################")
    print("##########################?????????#########################")
    print("#########***#####----Welcome To Aincrad----#####***#########")
    print("##########################?????????#########################")
    print("_______***--------Type your commands to do--------***_______")
    print("##########################?????????#########################")
    print("#***###***---------Use quit to leave game---------***###***#")
    print("##########################?????????#########################")
    print("#***###***---Use up, down, left, right, to move---***###***#")
    print("#*###***---Use north, south, west, north, to move---***###*#")
    print("#***###***----EX: '> move' THEN  EX: '> left' ----***###***#")
    print("##########################?????????#########################")
    print("_______*Use look, examine, inspect to inspect things*_______")
    print("#**###***----EX: '> look' THEN  EX: '> object' ----**###***#")
    print("##########################?????????#########################")
    print("#***###***---***Use fight to  battle enemies***---***###***#")
    print("#*- EX: '> fight' it randomly sees if you enter a battle -*#")
    print("##########################?????????#########################")
    print("#--Use stats to look at your att. def. inventory. .health--#")
    print("#*--- EX: '> stats' it prints  your att. def. inv. hp. ---*#")
    print("##########################?????????#########################")
    print("##########################?????????#########################")
    print("##########################HELP MENU#########################")
    title_scr_options()

#### Map of Aincrad ####
##############################
#                            #                   
#  1   2   3   4   5   6     #     
#-------------------------   #
#|   |   |   |   |   |   | a # 
#-------------------------   #
#|   |   |   |   |   |   | b # 
#-------------------------   #
#|   |   |   |   |   |   | c # 
#-------------------------   #
#|   |   |   |   |   |   | d # 
#-------------------------   # 
##############################

GET = True
AREANAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
ITEMS = ""
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
    
explored_areas = {"a1":False, "a2":False, "a3":False, "a4":False, "a5":False, "a6":False, 
                  "b1":False, "b2":False, "b3":False, "b4":False, "b5":False, "b6":False, 
                  "c1":False, "c2":False, "c3":False, "c4":False, "c5":False, "c6":False, 
                  "d1":False, "d2":False, "d3":False, "d4":False, "d5":False, "d6":False}

worldMap =  {
    "a1": {
        AREANAME: "TOWN Hall",
        DESCRIPTION: "The town hall is where the Lord and his serfs reside to hold meetings about the town, \n\
typically the lord of this town uses his time to dwell there \n\
come here if you want get a quest, the Lord has it posted on a wall",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2",
    },
   "a2": {
        AREANAME: "TOWN Marketplace",
        DESCRIPTION: "The marketplace is the most crowded place within the town. \n\
There is multiple shops in the marketplace: \n\
the medical shop ran by Joleen, the weapon shop ran by bob, \n\
the armor shop, and the clothing shop, but you aren't acquainted with those shop keepers.",
        EXAMINATION: {
            ITEMS: {
                "medical shop": "here is some medicine",
                "joleen": "here is some medicine",
                "weapon shop": "here is some weapons",
                "bob": "Bob is a old man with great knowledge of this world \n\
and profound skills at forging weapons, \n\
he looks at you and offers you a {}".format(item.item1),
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b2",
        LEFT:  "a1",
        RIGHT: "a3",
    },
    "a3": {
        AREANAME: "TOWN Square",
        DESCRIPTION: "The town square is a pretty sight to witness, \n\
it has a fountain located in the center and people surrounding it, \n\
a lady walks next to you and whispers in your hear something you barely remember \n\
you know the message she said was oddly familiar",
        EXAMINATION: {
            ITEMS: {
                "lady": "the lady is lost in the crowd, you can't seem to find her",
                "message": "the message said your destiny lies at the castle dungeon where you must fight the boss",
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b3",
        LEFT:  "a2",
        RIGHT: "a4",
    },
    "a4": {
        AREANAME: "TOWN Inn",
        DESCRIPTION: "The inn is a magical place where you can build up your strength, \n\
many adventures stop by here to get themselves back on their feet, \n\
there is a vase that rests upon a counter as soon as you enter the front door of the inn \n\
and behind the counter stands the owner of the inn, waiting patiently to check someone in.",
        EXAMINATION: {
            ITEMS: {
                "vase": "You look at the vase, the vase has bizzare patterns and made out of clay, \n\
it looks very valueable",
                "sleep": "The owner offers you a place to sleep, you spend the night in \n\
one of the rooms, you wake up and feel amazing, health has been replenished, +15 to hp",
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b4",
        LEFT:  "a3",
        RIGHT: "a5",
    },
    "a5": {
        AREANAME: "TOWN Gate",
        DESCRIPTION: "The gate is the entrance to the town, its also the most fortified and \n\
crawling with guards. This is where you check in to bring goods into the town to sell. \n\
One of the guards say to you 'Are you going to join the force, we need as many hands we can get', \n\
You reply some other time.",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b5",
        LEFT:  "a4",
        RIGHT: "a6",
    },
    "a6": {
        AREANAME: "TOWN Guard Outpost",
        DESCRIPTION: "There is five different barracks in the base, with various different boxes everywhere, \n\
Some of those boxes look like they hold something valueable. The outpost has many towers that overlook the town's gate. \n\
The guards currently are sleeping in their beds, so you take your time to not wake them up. \n\
There is a campfire off by itself that is cooking some food, there is no one around it.",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "",
        DOWN: "b6",
        LEFT:  "a5",
        RIGHT: "",
    },
    "b1": {
        AREANAME: "TOWN's Grave Yard",
        DESCRIPTION: "The graveyard is unkept leaving much of the area overgrown \n\
with plant life, many of the tombstones are unreadable, \n\
but there are a few left that are in good condition. \n\
Weirdly many of the graves look like they been robbed \n\
and no signs of tools were used to do so.",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "a1",
        DOWN: "c1",
        LEFT:  "",
        RIGHT: "b2",
    },
    "b2": {
        AREANAME: "CAVE",
        DESCRIPTION: "This place is dark to the point knowing what direction you're going is nearly imppossible, \n\
getting lost in here would probably be your end, so you navigate yourself towards the entrance \n\
There is a light reflecting off the walls in front of you from the entrance, \n\
you see the skeleton of someone whom must have \n\
gotten lost, what a shame.",
        EXAMINATION: {
            ITEMS: {
                "girl": "girl",
                },
            },
        SOLVED: False,
        UP: "a2",
        DOWN: "c2",
        LEFT:  "b1",
        RIGHT: "b3",
    },
    "b3": {
        AREANAME: "OLD SHACK",
        DESCRIPTION: "",
        EXAMINATION: {
            ITEMS: {
                "picture": "The picture is off center, \n it has blood stains all over it, \n its unclear what it used to be.",
                },
            },
        SOLVED: False,
        UP: "a3",
        DOWN: "c3",
        LEFT:  "b2",
        RIGHT: "b4",
    },
    "b4": {
        AREANAME: "DIRT PATH",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "a4",
        DOWN: "c4",
        LEFT:  "b3",
        RIGHT: "b5",
    },
    "b5": {
        AREANAME: "TOWN's South Gate Bridge",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "a5",
        DOWN: "c5",
        LEFT:  "b4",
        RIGHT: "b6",
    },
    "b6": {
        AREANAME: "FARM",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "a6",
        DOWN: "c6",
        LEFT:  "b5",
        RIGHT: "",
    },
    "c1": {
        AREANAME: "STEINFIELD CASTLE ENTRANCE",
        DESCRIPTION: "The castle is tremendous with statues everywhere and the monsters within been pillaging towns constantly, \n\
the castle reeks of blood, you approach the castle doors with caution, prepared for whatever may be behind the castle's metal doors, \n\
you open the doors and find dead bodies of monsters everywhere immediately on the other side of those doors",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "b1",
        DOWN: "d1",
        LEFT:  "",
        RIGHT: "c2",
    },
    "c2": {
        AREANAME: "WASTELAND",
        DESCRIPTION: "The wasteland is exactly how it sounds, there is no sign of plant or animal life \n\
it is too foggy to see anything, but you hear dreadful sounds all around you, \n\
also the sound of foot steps, but not yours trail behind you \n\
all you want to do is escape this horrific place.",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "b2",
        DOWN: "d2",
        LEFT:  "c1",
        RIGHT: "c3",
    },
    "c3": {
        AREANAME: "FORT MIGHTERDALE",
        DESCRIPTION: "The fort is old, but still standing, \n\
the guards let you in and give you a spiteful look. \n\
the fort has been struggling to defend the town from the monsters \n\
that lurk out of the castle from the south east. \n\
You pitty the old captain praying at the bodies of his fallen soldiers.",
        EXAMINATION: {
            ITEMS: {
                "fort": "the fort has taken a beating and has wooden gates protecting it, \n\
hopefully they remain solid while you visit...",
                "captain": "The Captain looks exhausted and covered in mud, head to toe, \n\
his eyes look dead while he prays for his fallen comrades, \n\
you struggle to find words to speak, but decide to remain silent",
                },
            },
        SOLVED: False,
        UP: "b3",
        DOWN: "d3",
        LEFT:  "c2",
        RIGHT: "c4",
    },
    "c4": {
        AREANAME: "LAKE OF WISDOM",
        DESCRIPTION: "The lake resides in a hazardous location, located in the middle of a battle zone, \n\
yet the enviroment is untouched and beautiful, \n\
the water stands still and the glow of the orb of tefeilese sits on the edge of the water, \n\
you thought it was just a myth.",
        EXAMINATION: {
            ITEMS: {
                "orb of tefeilese": "You approach the orb as its unique sparkle captures your focus. \n\
It's glow draws you towards it. You grab the grab the orb as it fades into nothingness. \n\
You gained wisdom, +3 to defense",
                },
            },
        SOLVED: False,
        UP: "b4",
        DOWN: "d4",
        LEFT:  "c3",
        RIGHT: "c5",
    },
    "c5": {
        AREANAME: "NO MANS LAND",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "b5",
        DOWN: "d5",
        LEFT:  "c4",
        RIGHT: "c6",
    },
    "c6": {
        AREANAME: "REDTAIL BANDIT HIDEOUT",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "b6",
        DOWN: "d6",
        LEFT:  "c5",
        RIGHT: "",
    },
    "d1": {
        AREANAME: "STEINFIELD CASTLE LOBBY",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "c1",
        DOWN: "",
        LEFT:  "",
        RIGHT: "d2",
    },
    "d2": {
        AREANAME: "STEINFIELD CASTLE ROOMS",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "c2",
        DOWN: "",
        LEFT:  "d1",
        RIGHT: "d3",
    },
    "d3": {
        AREANAME: "STEINFIELD CASTLE DUNGEON",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "boss": "the boss hears you approach and turns around",
                },
            },
        SOLVED: False,
        UP: "c3",
        DOWN: "",
        LEFT:  "d2",
        RIGHT: "d4",
    },
    "d4": {
        AREANAME: "",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT:  "d3",
        RIGHT: "d5",
    },
    "d5": {
        AREANAME: "",
        DESCRIPTION: "",
        EXAMINATION: {
            ITEMS: {
                "GIRL": "girl",
                },
            },
        SOLVED: False,
        UP: "c5",
        DOWN: "",
        LEFT:  "d4",
        RIGHT: "d6",
    },
    "d6": {
        AREANAME: "BLUE MOUNTAIN CAMP",
        DESCRIPTION: "description",
        EXAMINATION: {
            ITEMS: {
                "girl": "girl",
                },
            },
        SOLVED: False,
        UP: "c6",
        DOWN: "",
        LEFT: "d5",
        RIGHT: "",
    },

}


    
def prompt():
    print("\n" + "-----------------------")
    print("What do you wish to do?")
    print("-----------------------")
    action = input("> ")
    possible_actions = ["fight", "kill", "stats", "battle", "check stat", "check stats", "stats", "stat", "walk", "go", "move", "travel", "examine", "inspect", "interact", "look", "quit", "exit"]
    while action.lower() not in possible_actions:
        print("Enter a correct input")
        action = input("> ")
    if action.lower() in ["walk", "go", "travel", "move"]:
            character_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
            character_inspect(action.lower())
    elif action.lower() in ["check stat", "check stats", "stats", "stat"]:
            check_stats()
    elif action.lower() in ["fight", "kill", "battle"]:
            fight_mons()
    elif action.lower() in ["exit, quit"]:
            sys.exit()


def check_stats():
    print("\n" + "++++++++++++++++")
    print(character.name.upper() + " STATS: \n")
    print("ACTIVE QUEST:")
    quest.your_quests()
    print("HP: {:>11}".format(character.hp))
    print("ATTACK: {:>7}".format(character.attack))
    print("DEFENSE: {:>6}".format(character.defense))
    print("INVENTORY: ", inventory.inv)
    print("++++++++++++++++")
    prompt()
    

def fight_mons(): 
    rand = 1
    rand_mons = 0
    rand = random.randint(4,5)
    if rand == 5:
        rand_mons = random.randint(1,7)
        if rand_mons == 1:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Golbin")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Goblin")
            prompt()
        elif rand_mons == 2:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Hob-Golbin")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("HobGolbin")
            prompt()
        elif rand_mons == 3:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter an enemy, it's a Bandit")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Bandit")
            prompt()
        elif rand_mons == 4:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter an enemy, it's a Cult-Member")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("CultMember")
            prompt()
        elif rand_mons == 5:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Skeleton")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Skeleton")
            prompt()
        elif rand_mons == 6:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's an Andeddo")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Andeddo") 
            prompt()
        else:
            os.system('cls')
            print("\n" + "?????????????????????????????????????????????????")
            print("There isn't any enemy or monster around")
            print("Charging into battle is dangerous, be cautious...")
            print("?????????????????????????????????????????????????")
            prompt()
    else:
        os.system('cls')
        print("\n" + "?????????????????????????????????????????????????")
        print("There isn't any enemy or monster around")
        print("Charging into battle is dangerous, be cautious...")
        print("?????????????????????????????????????????????????")
        prompt()

def fight_boss(num): 
    num = 1
    if num == 1:
        os.system('cls')
        print("\n" + "!!!!!!!!!!!!!!!!!!!!!!")
        print("YOU ENCOUNTER YOUR FINAL BOSS")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        os.system('cls')
        print("The monster faces you and does a battle-cry, \n\
the monster is a HobGoblin that has taken the name of Monster of Destruction, \n\
brace youself for battle and pray to the greek gods to give you strength.")
        who_goes_first = 0
        enemy.hp = random.randint(50, 80)
        enemy.attack = random.randint(15, 30)
        enemy.defense = random.randint(15, 30)
        print("Your oppenents hp is {}".format(enemy.hp))
        while enemy.hp > 0 and character.hp > 0:
            enemy.attack = random.randint(15, 30)
            enemy.defense = random.randint(15, 30)
            who_goes_first = random.randint(1,2)
            if who_goes_first == 1:
                battle_enemy()
            elif who_goes_first == 2:
                battle_character()
        if enemy.hp <= 0:
            print("You Successfully beated the game, \n CONGRADULATIONS!!!")
        elif character.hp <= 0:
            you_died()
        
def random_encounter(): 
    rand = 1
    rand_mons = 0
    rand = random.randint(4,8)
    if rand == 8:
        rand_mons = random.randint(1,7)
        if rand_mons == 1:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Golbin")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Goblin")
        elif rand_mons == 2:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Hob-Golbin")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("HobGolbin")
        elif rand_mons == 3:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter an enemy, it's a Bandit")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Bandit")
        elif rand_mons == 4:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter an enemy, it's a Cult-Member")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("CultMember")
        elif rand_mons == 5:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's a Skeleton")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Skeleton")
        elif rand_mons == 6:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You Encounter a monster, it's an Andeddo")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            battle("Andeddo")
        elif rand_mons == 7:
            os.system('cls')
            print("\n" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("You got lucky, you Encountered a monster, but it fled")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    

def battle(name):
    print("YOU'RE IN A BATTLE!!")
    who_goes_first = 0
    enemy.name = name
    enemy.hp = random.randint(20, 30)
    enemy.attack = random.randint(10, 17)
    enemy.defense = random.randint(10, 17)
    print("Your oppenents hp is {}".format(enemy.hp))
    while enemy.hp > 0 and character.hp > 0:
        enemy.attack = random.randint(10, 17)
        enemy.defense = random.randint(10, 17)
        who_goes_first = random.randint(1,2)
        if who_goes_first == 1:
            battle_enemy()
        elif who_goes_first == 2:
            battle_character()
    if enemy.hp <= 0:
        you_win()
    elif character.hp <= 0:
        you_died()


def battle_enemy():
    print("The Enemy is attacking you!!")
    time.sleep(2)
    damage = int((enemy.attack * enemy.attack) / (enemy.attack + enemy.defense))
    character.hp = character.hp - damage
    if character.hp <= 0:
        character.hp = 0
    print("You took {} damage, \n Your health currently is {}".format(damage, character.hp))
    inp = input("> ")

def you_win():
    os.system('cls')
    print("You defeated the enemy!!")
    loot.loot_won()
    inp = input("> ")
    os.system('cls')
    prompt()

def battle_character():
    print("You attack the enemy!!")
    time.sleep(2)
    damage = int((character.attack * character.attack) / (character.attack + character.defense))
    enemy.hp = enemy.hp - damage
    if enemy.hp <= 0:
        enemy.hp = 0
    print("You dealt {} damage, \n The enemy's health currently is {}".format(damage, enemy.hp))
    inp = input("> ")

def you_died():
    print("...YOU ARE DEAD...")
    time.sleep(15)
    title_screen()

    
def print_location():
    print("------------------------")
    print(worldMap[character.location][AREANAME])
    print("------------------------")
    print(worldMap[character.location][DESCRIPTION])
    print("------------------------")
    prompt()

    
def character_move(action):
    print("\n" + "------------------------")
    print("Where do you wish to move?")
    print("------------------------")
    dest = input("> ")
    if dest.lower() in ["up", "north"]:
        destination = worldMap[character.location][UP]
        map_bounds(destination)
    elif dest.lower() in ["down", "south"]:
        destination = worldMap[character.location][DOWN]
        map_bounds(destination)
    elif dest.lower() in ["right", "east"]:
        destination = worldMap[character.location][RIGHT]
        map_bounds(destination)
    elif dest.lower() in ["left", "west"]:
        destination = worldMap[character.location][LEFT]
        map_bounds(destination)
    else:
        print("Enter a correct input!")
        prompt()

def map_bounds(destination):
    if destination == "":
        destination = worldMap[character.location]
        print("There is a cliff in your way, you can't proceed any further")
        prompt()
    else:
        movement_handler(destination)
    
    
def movement_handler(destination):
    os.system('cls')
    random_encounter()
    os.system('cls')
    character.location = destination
    print("\n" + "------------------------")
    print("YOU MOVED TO THE: {}".format(worldMap[character.location][AREANAME]))
    print("------------------------")
    print_location()

def character_inspect(action):
    print("\n" + "-------------------------------------")
    print("What/Where do you wanna inspect/look?")
    print("-------------------------------------")
    exam = input("> ")
    if exam.lower() in ["lady", "message", "boss", "sleep", "vase", "girl", "crying girl", "bob", "shop", "shop owner", "owner", "picture", "area", "room", "orb of tefeilese", "old captain", "captain", "fort"]:
        character.object = exam.lower()
        inspect_handler_printer(character.object)
        prompt()
    else:
        print("\n" + "There is nothing to see here...")
        prompt()

def inspect_handler_printer(characterObject):
    print("\n" + "-------------------------------------")
    print(worldMap[character.location][EXAMINATION][ITEMS][character.object])
    print("-------------------------------------")
    inventory_handler(character.object)

def inventory_handler(item):
    if character.object == "bob":
        if "SWORD" in inventory.inv:
            print("You already talked to bob")
        else: 
            inventory.inv.append("SWORD")
        quest.quest2 = True
    elif character.object == "orb of tefeilese":
        character.defense += 3
    elif character.object == "sleep":
        if character.hp < 140:
            character.hp += 15
    elif character.object == "message":
        quest.quest3 = True
    elif character.object == "boss":
        enemy.name = "Monster of Destruction"
        quest.quest4 = True
        fight_boss(1)
    else:
        print("...")

def game_setup():
    #INTRODUCTION:
    os.system('cls')
    character.hp = 100
    character.attack = 5
    character.defense = 5
    print("HELLO, WELCOME TO ELDERS SCROLL VI TEXT BASED ADVENTURE!")

    ######################SECTION 1: RACE OPTIONS

    race_ans = 0
    race_library = ["human", "dwarf", "orc", "high elf", "wood elf", "dark elf", "reptilian"]

    print("Race is an important characteristic in this RPG,")
    print("Each race has there own unique traits,")
    print("The Options Are:")

    while race_ans != "yes":
        for x in race_library:
            print("")
            print("{:>15}".format(x))
        print("")
        print("Enter Your Character Race")
        user_race = input("> ")
        user_race = user_race.lower()
        while user_race not in race_library:
            print("Enter one of the four races correctly")
            user_race = input("> ")
        print("You chose the race:",user_race)
        print("are you sure, yes or no:")
        race_ans = input("> ")
        
    print("You chose the race:",user_race.lower())
    character.race = user_race.lower()
    if user_race.lower() == "human" or user_race.lower() == "dwarf":
        character.hp += 10
        character.attack += 5
        character.defense += 6
    elif user_race.lower() == "orc" or user_race.lower() == "reptilian":
        character.hp += 15
        character.attack += 2
        character.defense += 3
    elif user_race.lower() == "high elf" or user_race.lower() == "wood elf" or user_race.lower() == "dark elf":
        character.hp += 5
        character.attack += 7
        character.defense += 8
            
    

    #####################SECTION 2: CLASS OPTIONS

    class_ans = 0
    class_library = ["knight","warrior","mercernary","bowman","assasin","theif","sorcerer","pyromancer"]
    
    print("")
    print("Classes is the type of character you will be in this RPG,")
    print("Each class has there own unique skills,")
    print("The Options Are:")

    print("")
    print("If you would like to see the details and the stats on a character class,")
    print("type the name of the class and '()' as one word, FOR EX. Warrior()")

    while class_ans != "yes":
        for x in class_library:
            print("")
            print("{:>15}".format(x))
 
        print("")
        print("Enter Your Character Class")
        user_class = input("> ")
        user_class = user_class.lower()
        while user_class.lower() not in class_library:
            print("Enter one of the eight classes correctly")
            user_class = input("> ")
        print("You chose the class:",user_class.lower())
        character.clas = user_class.lower()
        print("are you sure, yes or no:")
        class_ans = input("> ")


    print("\n" + "Enter Your Character Name")
    character.name = input("NAME: ")
    os.system('cls')
    print("\n" + "Hello {} the {}".format(character.name.upper(), user_class.upper()))
    if user_class == "knight" or user_class == "warrior":
        character.hp += 5
        character.attack += 10
        character.defense += 10
    elif user_class.lower() == "mercernary" or user_class.lower() == "bowman":
        character.hp += 10
        character.attack += 7
        character.defense += 9
    elif user_class.lower() == "assasin" or user_class.lower() == "theif":
        character.hp += 10
        character.attack += 8
        character.defense += 7
    elif user_class.lower() == "sorcerer" or user_class.lower() == "pyromancer":
        character.hp += 15
        character.attack += 7
        character.defense += 5 
    
    
class quest:
    def __init__(self):
        self.active = ""
        self.quest1 = True
        self.quest2 = False
        self.quest3 = False
        self.quest4 = False
        
    def your_quests(self):
        game_beat = False
        quest_main1 = "You lost your memory and only have bits and peices to put together. \n\
Proceed to the TOWN Marketplace and talk to bob and Joleen, the last people you remember."
        quest_main2 = "Talk to the woman at the times square, she might know your past."
        quest_main3 = "Go to the Steinfield castle dungeon and find the boss to achieve your purpose."
        quest_main4 = "You finished the game."
        if self.quest1 == True:
            self.active = quest_main1
            if self.quest2 == True:
                self.active = quest_main2
                if self.quest3 == True:
                    self.active = quest_main3
                    if self.quest4 == True:
                        self.active = quest_main4
                            
                        
            print(self.active)
            
quest = quest()

def start_game():
    game_setup()
    print("\n" + "++++++++++++++++")
    print(character.name.upper() + " STATS: \n")
    print("ACTIVE QUEST:")
    quest.your_quests()
    print("RACE: ", character.race)
    print("CLASS: ", character.clas)
    print("HP: {:>11}".format(character.hp))
    print("ATTACK: {:>7}".format(character.attack))
    print("DEFENSE: {:>6}".format(character.defense))
    print("INVENTORY: ", inventory.inv)
    print("++++++++++++++++")
    print("\n" + "YOU WAKE UP AT A...")
    print_location()

title_screen()
