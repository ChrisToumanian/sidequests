import random

class Dice:
    @staticmethod
    def roll(dice_notation, interaction):
        sides = int(dice_notation.split('d')[1].split("+")[0])

        if dice_notation[0] != 'd':
            n_dice = int(dice_notation.split('d')[0])
        else:
            n_dice = 1

        if "+" in dice_notation:
            bonus = int(dice_notation.split('d')[1].split("+")[1])
        else:
            bonus = 0

        rolls = []
        for i in range(n_dice):
            rolls.append(random.randint(1, sides))
        
        total = 0
        roll_str = ""
        for roll in rolls:
            total += roll
            roll_str += f"{roll} "
        
        total += bonus
        roll_str += f"+{bonus}"

        response = f"[🎲{dice_notation}] **{interaction.user.name}** rolls **{total}** ({roll_str})."

        if len(response) > 2000:
            response = f"[Error] **{dice_notation}** is invalid dice notation"
        
        return response
