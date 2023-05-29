import yaml
import psycopg2

class DatabaseConnection:
    def __init__(self):
        # Load the configuration file
        with open('settings/config.yaml', 'r') as f:
            data = yaml.safe_load(f)
        
        self.connection = psycopg2.connect(
            dbname=data["database"]["database"],
            user=data["database"]["user"],
            password=data["database"]["password"],
            host=data["database"]["host"]
        )

    def query(self, query_string):
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        cursor.close()
        return rows
