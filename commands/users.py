import yaml

class Users:
    
    @staticmethod
    def add_user(name, discord_username, id):
        # Load the configuration file
        with open('settings/config.yaml', 'r') as f:
            data = yaml.safe_load(f)

        # Check if user already exists
        for user in data["characters"]:
            if user["id"] == id:
                print(f"User with id {id} already exists")
                return

        # Create new user
        new_user = {
            "name": name,
            "discord_username": discord_username,
            "id": id
        }

        # Add new user to the existing list
        data["characters"].append(new_user)

        # Write updated data back to the file
        with open('settings/config.yaml', 'w') as f:
            yaml.safe_dump(data, f)

        print(f"User {name} has been added successfully")

    @staticmethod
    def remove_user(id):
        # Load the configuration file
        with open('settings/config.yaml', 'r') as f:
            data = yaml.safe_load(f)

        # Find and remove the user with the given id
        for i, user in enumerate(data["characters"]):
            if user["id"] == id:
                data["characters"].pop(i)
                print(f"User with id {id} has been removed successfully")
                break
        else:
            print(f"User with id {id} not found")

        # Write updated data back to the file
        with open('settings/config.yaml', 'w') as f:
            yaml.safe_dump(data, f)
