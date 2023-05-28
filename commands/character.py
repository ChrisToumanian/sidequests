import json
import yaml

class Character:
    def __init__(self, file_path, id, name, discord_username, data):
        self.file_path = file_path
        self.id = id
        self.name = name
        self.discord_username = discord_username
        self.data = data
    
    def get_balance(self):
        total_gp = 0
        total_gp += self.data["currencies"]["pp"] * 10
        total_gp += self.data["currencies"]["gp"]
        total_gp += self.data["currencies"]["ep"] / 2
        total_gp += self.data["currencies"]["sp"] / 10
        total_gp += self.data["currencies"]["cp"] / 100

        currencies = {
            "total": total_gp,
            "pp": self.data["currencies"]["pp"],
            "gp": self.data["currencies"]["gp"],
            "ep": self.data["currencies"]["ep"],
            "sp": self.data["currencies"]["sp"],
            "cp": self.data["currencies"]["cp"]
        }
        return currencies

class CharacterPool: 
    @staticmethod
    def load_characters():
        characters = []

        with open('settings/config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        # Load character JSON files to dictionaries
        for character in config["characters"]:
            file_path = "{}/{}.json".format(config["character_directory"], character["id"])
            data = CharacterPool.load_json_file(file_path)
            if data["success"]:
                new_character = Character(file_path, character["id"], character["name"], character["discord_username"], data["data"])
                characters.append(new_character)

        return characters
    
    @staticmethod
    def load_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    @staticmethod
    def get_character(characters, discord_username):
        for character in characters:
            if character.discord_username == discord_username:
                return character
