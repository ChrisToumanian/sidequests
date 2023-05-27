import os
import yaml
import requests

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def download_character_json(url, directory, filename):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(directory, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"'{filename}' downloaded successfully.")
    else:
        print(f"Failed to download JSON file. Status Code: {response.status_code}")

def main():
    # Load configuration
    config = load_config()

    # Pull latest character data from D&D Beyond
    for character in config["characters"]:
        url = "{}{}".format(config["dndbeyond"]["character_service_url"], character["id"])
        download_character_json(url, config["character_directory"], "{}.json".format(character["id"]))

if __name__ == "__main__":
    main()
