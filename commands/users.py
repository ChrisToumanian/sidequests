import yaml

class Users:
    @staticmethod
    def add_user(discord_username, dnd_beyond_id, db_conn):
        # Check if user is in database
        res = db_conn.query("""
            SELECT * FROM users WHERE username = %s;
        """, (discord_username,))

        if len(res) > 0:
            # User found, activate
            res = db_conn.execute("""
                UPDATE users SET activated = true WHERE username = %s;
            """, (discord_username,))
        else:
            # Create user 
            res = db_conn.execute("""
                INSERT INTO users (username) VALUES (%s);
            """, (discord_username,))

        # Create character
        Users.update_character(discord_username, dnd_beyond_id, db_conn)

        message = f"Player {discord_username} has been added successfully. Thank you for registering!"
        return message

    @staticmethod
    def remove_user(discord_username, db_conn):
        # Check if player is in database
        res = db_conn.query("""
            SELECT * FROM players WHERE username = %s;
        """, (discord_username,))

        if len(res) > 0:
            # Player found, so set to inactive
            res = db_conn.execute("""
                UPDATE players SET activated = false WHERE username = %s;
            """, (discord_username,))
            message = f"{discord_username} has been removed successfully. Thank you for playing!"
        else:
            # Player not found, send warning
            message = f"No player {discord_username} found. Were you signed up?"

        return message

    @staticmethod
    def update_character(discord_username, dnd_beyond_id, db_conn):
        res = db_conn.execute("""
            INSERT INTO characters (created_by_user_uuid, dnd_beyond_id)
            SELECT user_uuid, %s
            FROM users
            WHERE username = %s
            AND NOT EXISTS (
                SELECT 1
                FROM characters
                WHERE username = %s
                AND dnd_beyond_id = %s
            );

            UPDATE users
            SET current_character_uuid = (
                SELECT character_uuid
                FROM characters
                WHERE username = %s
                    AND dnd_beyond_id = %s
            );
        """, (dnd_beyond_id, discord_username, discord_username, dnd_beyond_id, discord_username, dnd_beyond_id))

        if res:
            return True
        else:
            return False
