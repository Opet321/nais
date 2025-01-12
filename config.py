import configparser
import os
from typing import Optional

CONFIG_FILE = "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_FILE)


def get_env_var(
    key: str, section: str = "APP_CONFIG", default: Optional[str] = None
) -> str:
    value = os.getenv(key)
    if value:
        return value

    if config.has_option(section, key):
        value = config.get(section, key).strip()
        if value:
            return value

    if default is not None:
        return default

    raise ValueError(f"Missing required configuration: {key}")


API_ID = int(get_env_var("API_ID", 16712780))
API_HASH = get_env_var("API_HASH", "7941450f5313966647b6d6fde5f933dc")
BOT_TOKEN = get_env_var("BOT_TOKEN", "7647918583:AAFRli68VM40AJJk_7-L4XZ2m5NFGDbSzU0") 
STRING_SESSION = get_env_var("SESSION_STRING", "BQD_BEwAXPDsQTHf-r4E25RviN6QmSlpZW4LtuHhCExYvF1mqj5JMipNOJ8Qwi1MQXSASoDGNJ9bSB8gAYHuNod7T4v2z9VLnZDZtXbQcEVizCiQqPJI-Ls823CzVdv5uegHyppJ-Mmsku6DG0kmFt2kxtT57xUj2vGn_TJstzad3ocETm82Q9WLyV86UB-C4QB3KqQDwUuEBBVIXsRzUINMow4V7ojT9g9b3q2PNrr-emUcpNZGfAHy3NyjFZ_hlMjm2uYXvUgziltdgq5IdU4D-kg6XoIgRcAeQLcqoTRVqpLeNA8F0dLRfG-u3XaAfr3cquf-NaoTjCFsMhyUSO7sfahWRQAAAAFw-KFTAA")
FORUM_CHAT_ID = int(get_env_var("FORUM_CHAT_ID", "-1002314627378"))
MONGODB_URL = get_env_var("MONGODB_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
