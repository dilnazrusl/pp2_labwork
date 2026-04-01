import psycopg2
from config import load_config
config = load_config()
try:
    conn = psycopg2.connect(**config)
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Error:", e)