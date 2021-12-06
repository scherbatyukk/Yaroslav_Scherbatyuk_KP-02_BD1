from model import do_Database_Changing
import psycopg2
from config import host, user, password, db_name, port


def Control_Input_Output(parameters):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        do_Database_Changing(parameters, connection)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed ")