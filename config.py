import os
from dotenv import load_dotenv


load_dotenv()

user_name = os.getenv('user_name')
access_key = os.getenv('access_key')
