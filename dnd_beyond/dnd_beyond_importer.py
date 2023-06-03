import yaml
import requests

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
            DNDBeyondImporter.load_character(dnd_beyond_id, db_conn, response.content)
        else:
            print(f"Failed to download JSON file. Status Code: {response.status_code}")

    def load_character(user_uuid, dnd_beyond_id, db_conn, data):
        print(data["name")
