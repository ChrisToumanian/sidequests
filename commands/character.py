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

    def get_details(self):
        details = {
            "name": self.data["name"],
            "gender": self.data["gender"],
            "race": self.data["race"],
            "faith": self.data["faith"],
            "age": self.data["age"],
            "hair": self.data["hair"],
            "eyes": self.data["eyes"],
            "skin": self.data["skin"],
            "height": self.data["height"],
            "weight": self.data["weight"]
        }
        return details
    
    def get_notes(self):
        return self.data["notes"]

    def get_traits(self):
        return self.data["traits"]
    
    def get_inventory(self):
        return self.data["inventory"]

    def get_classes(self):
        return self.data["classes"]

    def get_campaign(self):
        return self.data["campaign"]

    def get_stats(self):
        stats = {
            "strength": self.data["stats"][0]["value"],
            "dexterity": self.data["stats"][1]["value"],
            "constitution": self.data["stats"][2]["value"],
            "intelligence": self.data["stats"][3]["value"],
            "wisdom": self.data["stats"][4]["value"],
            "charisma": self.data["stats"][5]["value"],
            "proficiency_bonus": 0,
            "walking_speed": 0,
            "initiative": 0
        }
        return abilities

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
