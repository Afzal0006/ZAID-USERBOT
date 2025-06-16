import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwPRkAKOB08pWhlQn1BwiNMK8RlTaBp6CVphq76CC447VIYi63CcRU1qd61BfdwiR1anqvicoEjN8Dti73Mir6ohVYT81ZBeMiy4ccN1eg4MVQA9toGV3PXIhsZ7bIblIMg0_5OJ07Uvpx5_HeGhG6Q8_kmBX0snL18cieMbIXbO3q5RXF-Pc3ZwY-AY2rfiqIcFU0SuglSp0yGYOM7l4PsCoUCjd1ELcWIb-NnO3bThCdMhMaLV19QKNLeIoZqlnIq_9idDkmq4t9b7Mt9Yf7ZMFUmlYtstND65GfSUZb2iUGBO76yl57BBMdqmNSKauCP49jAoQ8DOri3-a79OGiIitbyAAAAAHceB2jAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
