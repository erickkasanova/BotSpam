import os
from dotenv import load_dotenv

load_dotenv()
sudo = []

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
string = os.environ.get("STRING_SESSION")
semx = os.environ.get("USER_ID")
sudo.append(int(semx))
