import os
import logging
import subprocess
from sesi import TG_BOT_TOKEN, api_id, api_hash, tg_user_session_name, auth_users


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", TG_BOT_TOKEN)

    # Get from sesi.py
    APP_ID = int(os.environ.get("APP_ID", api_id))

    # Get from sesi.py
    API_HASH = os.environ.get("API_HASH", api_hash)

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", " ".join(auth_users)).split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", tg_user_session_name)

    # Read session string from session_string.txt if it exists
    if os.path.exists("session_string.txt"):
        with open("session_string.txt", "r") as file:
            session_string = file.read().strip()
    else:
        session_string = ""

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", session_string)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
