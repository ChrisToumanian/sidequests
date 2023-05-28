import yaml
import discord
from discord import app_commands
from discord.ext import commands
from commands.character_stats import CharacterStats
from commands.dice import Dice
from commands.magic_eight_ball import Magic8Ball
from dnd_beyond.download_characters import DownloadCharacters
from commands.character import Character, CharacterPool

# Import config
def load_config():
    with open('settings/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load characters
characters = CharacterPool.load_characters()

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
@bot.tree.command(name="update")
async def update(interaction: discord.Interaction):
    try:
        download_characters = DownloadCharacters()
        download_characters.download()
        await interaction.response.send_message("Characters downloaded from D&D Beyond and updated!")
    except Exception as e:
        print(e)

@bot.tree.command(name="roll")
@app_commands.describe(dice="What type of dice? (d20, d6, 2d12, 3d4+2 etc.)")
async def roll(interaction: discord.Interaction, dice:str):
    global characters
    try:
        username = interaction.user.name
        for character in characters:
            if character.discord_username == username:
                username = character.name
        message = Dice.roll_verbose(username, dice) 
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

@bot.tree.command(name="balance")
async def balance(interaction: discord.Interaction):
    global characters
    try:
        character = CharacterPool.get_character(characters, interaction.user.name)
        if character != None:
            currencies = character.get_balance()
            message = f"{character.name} has {currencies['total']} GP."
        else:
            message = "Character not found! Have you signed up to our D&D campaign?"
        await interaction.response.send_message(message, ephemeral=False)
    except Exception as e:
        print(e)

@bot.tree.command(name="characters")
async def print_character_stats(interaction: discord.Interaction):
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
