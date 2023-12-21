import os
from dotenv import load_dotenv


load_dotenv()

context = os.getenv('context', 'bstack')
user_name = os.getenv('user_name')
access_key = os.getenv('access_key')
remote_browser_url = os.getenv('remote_browser_url')
