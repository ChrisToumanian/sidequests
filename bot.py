import discord
from discord import app_commands
from discord.ext import commands
import yaml
import random
import character_stats

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# import config
config = load_config()
token = config['discord']['token']

# create bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Sidequests Discord Bot is now running")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="roll")
@app_commands.describe(dice="What type of dice? (d20, d6, 2d12, 3d4+2 etc.)")
async def roll(interaction: discord.Interaction, dice:str):
    try:
        sides = int(dice.split('d')[1].split("+")[0])

        if dice[0] != 'd':
            n_dice = int(dice.split('d')[0])
        else:
            n_dice = 1

        if "+" in dice:
            bonus = int(dice.split('d')[1].split("+")[1])
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

        message = f"[🎲{dice}] **{interaction.user.name}** rolls **{total}** ({roll_str})."

        if len(message) > 2000:
            message = f"[Error] **{dice}** is invalid dice notation"
    
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

@bot.tree.command(name="characters")
async def hello(interaction: discord.Interaction):
    message = character_stats.get_character_stats()
    await interaction.response.send_message(message, ephemeral=False)

@bot.tree.command(name="magic8ball")
async def roll(interaction: discord.Interaction):
    try:
        responses = [
            "IT IS CERTAIN",
            "IT IS DECIDEDLY SO",
            "WITHOUT A DOUBT",
            "YES DEFINITELY",
            "YOU MAY RELY ON IT",
            "AS I SEE IT, YES",
            "MOST LIKELY",
            "OUTLOOK GOOD",
            "YES",
            "SIGNS POINT TO YES",
            "REPLY HAZY, TRY AGAIN",
            "ASK AGAIN LATER",
            "BETTER NOT TELL YOU NOW",
            "CANNOT PREDICT NOW",
            "CONCENTRATE AND ASK AGAIN",
            "DON'T COUNT ON IT",
            "MY REPLY IS NO",
            "MY SOURCES SAY NO",
            "OUTLOOK NOT SO GOOD",
            "VERY DOUBTFUL"
        ]
        answer = random.randint(0,19)
        message = responses[answer]
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

bot.run(token)
