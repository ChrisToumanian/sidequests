import yaml
import requests
import json

class DNDBeyondImporter:
    @staticmethod
    def load_config():
        with open('settings/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config

    @staticmethod
    def import_character(user_uuid, dnd_beyond_id, db_conn):
        config = DNDBeyondImporter.load_config()
        url = "{}{}".format(config["dndbeyond"]["character_service_url"], dnd_beyond_id)

        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)["data"]
            DNDBeyondImporter.load_character(user_uuid, dnd_beyond_id, db_conn, data)
            return True
        else:
            print(f"Failed to download JSON file. Status Code: {response.status_code}")
            return False

    @staticmethod
    def load_character(user_uuid, dnd_beyond_id, db_conn, data):
        print(data["name"])