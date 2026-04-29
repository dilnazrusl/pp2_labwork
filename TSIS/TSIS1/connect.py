import psycopg2
from config import load_config

def get_conn():
    config = load_config()
    return psycopg2.connect(**config)