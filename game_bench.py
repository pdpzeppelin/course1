from copy import deepcopy

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


def _user_input(question):
    user_input = input(f"{question}: ")
    user_input = int(user_input)
    return user_input

def _heal():
    print(
        """
        1. Lesser Heal
        2. Greater Heal
        """
    )

    user_input = _user_input("Please choose a heal")
    spell = ACTIONS[1]['spells'][user_input]
    return spell

def choose_action():
    action_text = """
        1. Heal
        2. Attack
    """

    print(action_text)

    user_input = _user_input("Please choose a action")

    action = deepcopy(ACTIONS[user_input])
    
    if user_input == 1:
        heal = _heal()
        print (heal)



choose_action()