import yaml

class Users:
    @staticmethod
    def add_user(discord_username, dnd_beyond_id, db_conn):
        result = db_conn.execute("""
            INSERT INTO players (username) VALUES (%s);
        """, (discord_username,))

        if result:
            response = f"Player {discord_username} has been added successfully"
        else:
            response = f"Error adding {discord_username}"

        return response

    @staticmethod
    def remove_user(discord_username, db_conn):
        result = db_conn.execute("""
            DELETE FROM players WHERE username = %s;
        """, (discord_username,))
        
        if result:
            response = f"User {discord_username} has been removed successfully"
        else:
            response = f"Error removing {discord_username}. Were you signed up?"

        return response
