import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

DB_CONFIG = {
    'dbname': 'local',
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',
    'port': '5432'   
 }
