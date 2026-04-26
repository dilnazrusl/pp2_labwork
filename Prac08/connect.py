import psycopg2
from config import config

# config = load_config()

def connect():
    print("form connect")
    try:
        conn = psycopg2.connect(**config)
        print("Connected successfully!")
        # conn.close()
        return conn
    except Exception as e:
        print("Error:", e)
        return None