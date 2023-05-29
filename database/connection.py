import yaml
import psycopg2
from psycopg2 import pool

class DatabaseConnection:
    def __init__(self):
        with open('settings/config.yaml', 'r') as f:
            data = yaml.safe_load(f)
        
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
            dbname=data["database"]["database"],
            user=data["database"]["user"],
            password=data["database"]["password"],
            host=data["database"]["host"]
        )

    def query(self, query_string, params=None):
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query_string, params)
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                return result
        finally:
            self.connection_pool.putconn(conn)

    def execute(self, query_string, params=None):
        # Use parameterized queries
        # Example: conn.execute("INSERT INTO players (username) VALUES (%s)", ("username",))
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query_string, params)
                conn.commit()
                return cursor.rowcount >= 1
        finally:
            self.connection_pool.putconn(conn)
