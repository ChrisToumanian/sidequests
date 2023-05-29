import random
import json
from commands.dice import Dice

class Fishing:
    @staticmethod
    def fish(character):
        # Cast
        response = f"{character.name} performs a nature check to cast a fishing line."
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)
        response += f"\n{roll}"

        if total < 6:
            response += f"\n{character.name} waits but nothing bites."
            return f"```{response}```"

        # Reel
        response += f"\n{character.name} feels a bite and does a strength check to reel it in."
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)
        response += f"\n{roll}"

        if total < 8:
            response += f"\nThe fish gets away."
            return f"```{response}```"
 
        # Catch
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)

        item = Fishing.loot()
        response += f"\n{character.name} catches a {item['name']}! {item['description']}"
 
        return f"```{response}```"

    @staticmethod
    def loot():
        # Load the JSON file
        with open('data/loot/fish.json') as json_file:
            loot_table = json.load(json_file)['loot_table']
        
        roll = random.randint(0, len(loot_table) - 1)

        return loot_table[roll]
