import random
from commands.dice import Dice

class Fishing:
    @staticmethod
    def fish(character):
        # Cast
        response = f"{character.name} performs a nature check to cast a fishing line."
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)
        response += f"\n{roll}"

        if total < 10:
            response += f"\n{character.name} waits but but nothing bites."
            return f"```{response}```"

        # Reel
        response += f"\n{character.name} feels a bite and does a strength check to reel it in."
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)
        response += f"\n{roll}"

        if total < 6:
            response += f"\nThe fish gets away."
            return f"```{response}```"
 
        # Catch
        loot = "Carp"
        dice = "d20"
        roll, total = Dice.roll_verbose(character.name, dice)

        item = Fishing.loot()
        response += f"\n{character.name} catches a {item['name']}, worth {item['value']} GP. {item['description']}!"
 
        return f"```{response}```"

    @staticmethod
    def loot():
        # Load the JSON file
        with open('data/loot/fish.json') as json_file:
            loot_table = json.load(json_file)

        # Roll for loot
        loot_roll = random.uniform(0, 100)

        for item in loot_table['loot_table']:
            if loot_roll <= item['loot_percentage']:
                return item
        return None
