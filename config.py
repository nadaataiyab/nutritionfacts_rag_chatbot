import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the absolute path to the directory where config.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to your database file
SQL_DATABASE_PATH = os.path.join(BASE_DIR, 'data', 'nutrition_data.db')
