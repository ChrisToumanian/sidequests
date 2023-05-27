import yaml
import discord
from discord import app_commands
from discord.ext import commands
from commands.character_stats import CharacterStats
from commands.dice import Dice
from commands.magic_eight_ball import Magic8Ball

# Import config
def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Create bot
config = load_config()
token = config['discord']['token']
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Event
@bot.event
async def on_ready():
    print("Sidequests Discord Bot is now running")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Commands
@bot.tree.command(name="roll")
@app_commands.describe(dice="What type of dice? (d20, d6, 2d12, 3d4+2 etc.)")
async def roll(interaction: discord.Interaction, dice:str):
    try:
        message = Dice.roll_verbose(interaction, dice) 
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

@bot.tree.command(name="characters")
async def hello(interaction: discord.Interaction):
    try:
        character_stats = CharacterStats()
        message = character_stats.get_character_stats()
        await interaction.response.send_message(message, ephemeral=False)
    except Exception as e:
        print(e)

@bot.tree.command(name="magic8ball")
async def roll(interaction: discord.Interaction):
    try:
        message = Magic8Ball.toss()
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

# Initialization
def run():
    bot.run(token)
