# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28795738"))
API_HASH = os.environ.get("API_HASH", "1543cd4c2182127e949590c86895b5c0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5840149821:AAG_0TaEQi3YBUz7LgH2MPVTGhtiXvqJRPE")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("2078079624")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Ahammad")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://anismia01707:<anis4342>@cluster0.3ixab5y.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "2078079624")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id-1001930912280")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Unique Movies Hub বেকাপ Backup.") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
