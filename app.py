import os

import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def get_users():
    conn = psycopg2.connect(
        os.environ["DATABASE_URL"]
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pg_user')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
