import json
import yaml

class CharacterStats:
    def __init__(self):
        self.characters = []

    def load_config(self):
        with open('settings/config.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def load_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def get_character_stats(self):
        # Load configuration
        self.load_config()

        # Load character JSON files to dictionaries
        for character in self.config["characters"]:
            file_path = "{}/{}.json".format(self.config["character_directory"], character["id"])
            data = self.load_json_file(file_path)
            if data["success"]:
                self.characters.append(data["data"])
        
        # Check each character
        message = "D&D Beyond Characters:"
        for character in self.characters:
            message += f"\n\n{character['name']}"

            for c in character["classes"]:
                message += f"\nLevel {c['level']} {c['definition']['name']}"

            total_gp = 0
            total_gp += character["currencies"]["pp"] * 10
            total_gp += character["currencies"]["gp"]
            total_gp += character["currencies"]["ep"] / 2
            total_gp += character["currencies"]["sp"] / 10
            total_gp += character["currencies"]["cp"] / 100
            message += f"\nGold: {total_gp}"

        response = f"```{message}```"

        return response
