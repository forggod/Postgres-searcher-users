import os

import psycopg2

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
