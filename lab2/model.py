import psycopg2
from config import host, user, password, db_name, port


def do_Database_Changing(parameters, connection):

        # the cursor for performing database operations
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f"Server version: {cursor.fetchone()}")
            print(parameters)

