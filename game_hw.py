import random

from copy import deepcopy

# make dictionaries for user class
# add in key for mana, rage, energy user
# separate into separate sub-dictionaries

CLASSES = {
    1: {
        "name": "Mage",
        "intellect": 150,
        "spirit": 10,
        "hp": 100,
        "mana": 150,
    },
    2: {
        "name": "Warlock",
        "intellect": 130,
        "spirit": 8,
        "hp": 100,
        "mana": 125,
    },
    3: {
        "name": "Priest",
        "intellect": 100,
        "spirit": 20,
        "hp": 100,
        "mana": 110,
    },
    4: {
        "name": "Shaman",
        "intellect": 110,
        "spirit": 112,
        "hp": 100,
        "mana": 100,
    }
}

MOBS = [
    {
        "name": "Archer",
        "hp": 100,
        "mana": 100,
    },
    {
        "name": "Warrior",
        "hp": 120,
        "mana": 0,
    },
    {
        "name": "Healer",
        "hp": 100,
        "mana": 100,
    },
    {
        "name": "Spell Caster",
        "hp": 100,
        "mana": 120,
    }
]

ACTIONS = {
    1: {
        "name": "Heal",
        "spells": {
            1: {
                "name": "Lesser Heal",
                "value": 10,
            },
            2: {
                "name": "Greater Heal",
                "value": 19,
            },
        },
    },
    2: {
        "name": "Attack",
        "spells": {
            1: {
                "name": "Quick Attack",
                "value": 10,
            },
            2: {
                "name": "Slow Attack",
                "value": 15,
            },
        }
    }
}



def choose_action():
    action_text = """
        1. Heal
        2. Attack
        """
    print(action_text)

def choose_class():
    classes_text = """
    1. Mage
    2. Warlock
    3. Priest
    4. Shaman
    """
    print(classes_text)

    chosen_class = input(
        "Please choose a mana using class to fight your battle: "
    )

    try:
        chosen_class = int(chosen_class)
    except ValueError:
        print("You need to input a valid number between 1 and 4")
        return 0
    else:
        if chosen_class > 4:
            print(f"{chosen_class} is greather than 4")
            return 0
        else:
            return chosen_class



# If chosen_class < 1:
#           print(f"{chosen_class} must be larger than zero")
#            return 0


finished = False

while finished == False:
    chosen_class = choose_class()

    if chosen_class > 0:
        character = deepcopy(CLASSES[chosen_class])
        character_name = character['name']

        print(f"You chose the {character_name} class! Be careful out there!")

        alive = True

        while alive == True:
            mob = deepcopy(random.choice(MOBS))
            mob_name = mob["name"]
            mob_hp = mob['hp']
            fighting = False

            print(
                f"You are fighting {mob_name} with {mob_hp} hp! Try not to die...")

            ACTIONS = input(int(ACTIONS))
            print("Choose your next {ACTIONS} ")

    

            alive = False
