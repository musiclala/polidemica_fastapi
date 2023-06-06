import psycopg2 as psycopg2
import dotenv
import os


dotenv.load_dotenv('.env')

conn = psycopg2.connect(host=os.environ['host'], port=os.environ['port'], database=os.environ['database'], user=os.environ['user'],
                            password=os.environ['password'])


def open_db():
    cursor = conn.cursor()

    return cursor


def close_db(open_db):
    conn.commit()
    open_db.close()