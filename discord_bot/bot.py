import yaml
import discord
from discord import app_commands
from discord.ext import commands
from commands.dice import Dice
from commands.magic_eight_ball import Magic8Ball
from dnd_beyond.download_characters import DownloadCharacters
from commands.character import Character, CharacterPool
from commands.users import Users
from commands.fishing import Fishing

# ----------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------
# D&D Character Registration and updates
# ----------------------------------------------------------------------------------
@bot.tree.command(name="update")
async def update(interaction: discord.Interaction):
    try:
        download_characters = DownloadCharacters()
        download_characters.download()
        await interaction.response.send_message("Characters downloaded from D&D Beyond and updated!")
    except Exception as e:
        print(e)

@bot.tree.command(name="register")
@app_commands.describe(dnd_beyond_id="The 9-digit D&D Beyond character ID from the URL.", character_name="The name of your character")
async def register(interaction: discord.Interaction, dnd_beyond_id:int, character_name:str):
    global characters
    try:
        message = Users.add_user(character_name, interaction.user.name, dnd_beyond_id)
        characters = CharacterPool.load_characters()
        await interaction.response.send_message(message, ephemeral=False)
    except Exception as e:
        print(e)

@bot.tree.command(name="unregister")
async def register(interaction: discord.Interaction):
    global characters
    try:
        character = CharacterPool.get_character(characters, interaction.user.name)
        if character != None:
            message = Users.remove_user(character.id)
            characters = CharacterPool.load_characters()
        else:
            message = "Character not found! You have not registered."
        await interaction.response.send_message(message, ephemeral=False)
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------
# D&D Character Stats
# ----------------------------------------------------------------------------------
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

@bot.tree.command(name="stats")
async def print_character_stats(interaction: discord.Interaction):
    global characters
    try:
        character = CharacterPool.get_character(characters, interaction.user.name)
        details = character.get_details()
        classes = character.get_classes()
        abilities = character.get_abilities()

        msg = details["name"]
        if details["gender"] != None:
            msg += f"\n{details['gender']} {details['race']}"
        else:
            msg += f"\n{details['race']}"

        for c in classes:
            msg += f"\nLevel {c['level']} {c['definition']['name']}\n"
        
        msg += f"\nStrength: {abilities['strength']}"
        msg += f"\nDexterity: {abilities['dexterity']}"
        msg += f"\nConstitution: {abilities['constitution']}"
        msg += f"\nIntelligence: {abilities['intelligence']}"
        msg += f"\nWisdom: {abilities['wisdom']}"
        msg += f"\nCharisma: {abilities['charisma']}"

        await interaction.response.send_message(f"```{msg}```", ephemeral=False)
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------
# Minigames
# ----------------------------------------------------------------------------------
@bot.tree.command(name="fish")
async def roll(interaction: discord.Interaction):
    global characters
    try:
        character = CharacterPool.get_character(characters, interaction.user.name)
        message = Fishing.fish(character)
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------------------
@bot.tree.command(name="roll")
@app_commands.describe(dice="What type of dice? (d20, d6, 2d12, 3d4+2 etc.)")
async def roll(interaction: discord.Interaction, dice:str):
    global characters
    try:
        username = interaction.user.name
        for character in characters:
            if character.discord_username == username:
                username = character.name
        message, total = Dice.roll_verbose(username, dice) 
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

@bot.tree.command(name="magic8ball")
async def roll(interaction: discord.Interaction):
    try:
        message = Magic8Ball.toss()
        await interaction.response.send_message(message)
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------
# Initialization
# ----------------------------------------------------------------------------------
def run():
    bot.run(token)
