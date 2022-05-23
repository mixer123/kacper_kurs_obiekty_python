from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()
print('FIRST_NAME', getenv('FIRST_NAME'))