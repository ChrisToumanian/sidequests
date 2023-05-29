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
                response = f"User with id {id} already exists"
                return response

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

        response = f"User {name} has been added successfully"
        return response

    @staticmethod
    def remove_user(id):
        # Load the configuration file
        with open('settings/config.yaml', 'r') as f:
            data = yaml.safe_load(f)

        # Find and remove the user with the given name
        for i, user in enumerate(data["characters"]):
            if user["id"] == id:
                data["characters"].pop(i)
                break
        else:
            response = f"User with id {id} not found"
            return response

        # Write updated data back to the file
        with open('settings/config.yaml', 'w') as f:
            yaml.safe_dump(data, f)
        
        response = f"User with id {id} has been removed successfully"
        return response
