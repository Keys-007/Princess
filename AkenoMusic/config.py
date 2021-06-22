import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQA8htAO_Z18aRkHdP1Q3MNDE_cXhqA8o4-V6vDEBa4KD8AElupEDSl2zQkhOhxu3QJkpy1shi2zmAVizGijq1VTxD2UzR9Dc1_xmRMeWve3rO4-TzPEZTw2IZxhahnCnX9D-5vUddixhpsJ2S8KLW9tsN-Uf1GhBONISmicRuZD8ZUZH1ToBjSvnxBwtahNqD7LrcvTmCQn4mRGDtnj8tIdB8BM_dsUab8TyJwpfWgb_9QTCWe8T7IythU8ertOlHnDEVfg-FC-S9XUlNfLuK4UWEb26hfVWkrvjVHNPP_xyWwQAShjRUDSfuX8q0wTlGDNfrqVNrNCNn8lx7MF9WMBW50AxgA"
BOT_TOKEN = "1771297531:AAEcyxO9LjBwK8QYv0Nq8-Ibqimg6rTGXQ8"
BOT_NAME = "HybridMusicRobot"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@akenoXsupport")
BG_IMAGE =getenv("BG_IMAGE", "https://telegra.ph/file/af1e8f26868716695766e.jpg")
admins = {}
API_ID = 3325295
API_HASH = "c8e4335cb03e21e5abd2a12d01b67462"

DURATION_LIMIT = getenv("DURATION_LIMIT", "7")
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ? !").split())

SUDO_USERS = 1603318426
