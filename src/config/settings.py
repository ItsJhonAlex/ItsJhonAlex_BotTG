import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Convertir la cadena de usuarios autorizados en una lista de enteros
AUTHORIZED_USERS = [
    int(user_id.strip())
    for user_id in os.getenv("AUTHORIZED_USERS", "").split(",")
    if user_id.strip()
]

