import json
import yaml

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_character_stats():
    # Load configuration
    config = load_config()

    # Load character JSON files to dictionaries
    characters = []
    for character in config["characters"]:
        file_path = "{}/{}.json".format(config["character_directory"], character["id"])
        data = load_json_file(file_path)
        if data["success"]:
            characters.append(data["data"])
    
    # Check each character
    message = "D&D Beyond Characters:"
    for character in characters:
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

    return f"```{message}```"
