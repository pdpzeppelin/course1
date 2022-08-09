import random

from copy import deepcopy

CLASSES = [
    {
        "name": "Mage",
        "intellect": 150,
        "spirit": 10,
        "hp": 100,
        "mana": 150,
    },
    {
        "name": "Warlock",
        "intellect": 130,
        "spirit": 8,
        "hp": 100,
        "mana": 125,
    },
    {
        "name": "Priest",
        "intellect": 100,
        "spirit": 20,
        "hp": 100,
        "mana": 110,
    },
    {
        "name": "Shaman",
        "intellect": 110,
        "spirit": 112,
        "hp": 100,
        "mana": 100,
    }
]

ACTIONS = [
    {
        "name": "Heal",
        "spells": [
            {
                "name": "Lesser Heal",
                "value": 10,
                "operation": "plus"
            },
            {
                "name": "Greater Heal",
                "value": 19,
                "operation": "plus"
            },
        ]
    },
    {
        "name": "Attack",
        "spells": [
            {
                "name": "Quick Attack",
                "value": 10,
                "operation": "minus"
            },
            {
                "name": "Slow Attack",
                "value": 15,
                "operation": "minus"
            },
        ]
    }
]

MOBS = [
    {
        "name": "Archer",
        "hp": 100,
        "mana": 100,
        "spell": {
            "value": 3,
            "operation": "minus"
        }
    },
    {
        "name": "Warrior",
        "hp": 120,
        "mana": 0,
        "spell": {
            "value": 3,
            "operation": "minus"
        }
    },
    {
        "name": "Healer",
        "hp": 100,
        "mana": 100,
        "spell": {
            "value": 3,
            "operation": "minus"
        }
    },
    {
        "name": "Spell Caster",
        "hp": 100,
        "mana": 120,
        "spell": {
            "value": 3,
            "operation": "minus"
        }
    }
]


def _random_choice(items):
    return deepcopy(random.choice(items))


def _user_input(question):
    user_input = input(f"{question}: ")
    user_input = int(user_input)
    user_input = user_input - 1
    return user_input


def _user_choice(items, title, user_input_message):
    print(title)

    index = 0

    for item in items:
        print(f"{index + 1}. {item['name']}")
        index = index + 1

    user_input = _user_input(user_input_message)

    return deepcopy(items[user_input])


def _cast(target, spell):
    if spell['operation'] == 'plus':
        return target['hp'] + spell['value']
    elif spell['operation'] == 'minus':
        return target['hp'] - spell['value']

player = _user_choice(CLASSES, "Classes", "Please choose your class")

mob = _random_choice(MOBS)

print (f"You are fighting {mob['name']}")

action = _user_choice(ACTIONS, "Actions", "Choose your action")

player_spell = _user_choice(action['spells'], "Spells", "Choose your spell")

print (f"Before Player HP: {player['hp']}")
print (f"Before Mob HP: {mob['hp']}")

if action['name'] == "Heal":
    player['hp'] = _cast(player, player_spell)
elif action['name'] == "Attack":
    player['hp'] = _cast(player, mob['spell'])
    mob['hp'] = _cast(mob, player_spell)
 
print (f"After Player HP: {player['hp']}")
print (f"After Mob HP: {mob['hp']}")

# build new dictionary + functions to call dictionaries + indexes