import yaml

class Users:
    @staticmethod
    def add_user(discord_username, dnd_beyond_id, db_conn):
        result = db_conn.execute("""
            INSERT INTO players (username) VALUES (%s);
        """, (discord_username,))
        # Load the configuration file
        # with open('settings/config.yaml', 'r') as f:
        #     data = yaml.safe_load(f)

        # # Check if user already exists
        # for user in data["characters"]:
        #     if user["id"] == id:
        #         response = f"User with id {id} already exists"
        #         return response

        # # Create new user
        # new_user = {
        #     "name": name,
        #     "discord_username": discord_username,
        #     "id": id
        # }

        # # Add new user to the existing list
        # data["characters"].append(new_user)

        # # Write updated data back to the file
        # with open('settings/config.yaml', 'w') as f:
        #     yaml.safe_dump(data, f)

        if result:
            response = f"Player {discord_username} has been added successfully"
        else:
            response = f"Error adding {discord_username}"

        return response

    @staticmethod
    def remove_user(discord_username, db_conn):
        result = db_conn.execute("""
            DELETE FROM players (username) VALUES (%s);
        """, (discord_username,))
        # # Load the configuration file
        # with open('settings/config.yaml', 'r') as f:
        #     data = yaml.safe_load(f)

        # # Find and remove the user with the given name
        # for i, user in enumerate(data["characters"]):
        #     if user["discord_username"] == discord_username:
        #         data["characters"].pop(i)
        #         break
        # else:
        #     response = f"User with username {discord_username} not found"
        #     return response

        # # Write updated data back to the file
        # with open('settings/config.yaml', 'w') as f:
        #     yaml.safe_dump(data, f)
        
        if result:
            response = f"User {discord_username} has been removed successfully"
        else:
            response = f"Error removing {discord_username}. Were you signed up?"

        return response
