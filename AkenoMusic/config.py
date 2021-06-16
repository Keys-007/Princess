import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQA8htAO_Z18aRkHdP1Q3MNDE_cXhqA8o4-V6vDEBa4KD8AElupEDSl2zQkhOhxu3QJkpy1shi2zmAVizGijq1VTxD2UzR9Dc1_xmRMeWve3rO4-TzPEZTw2IZxhahnCnX9D-5vUddixhpsJ2S8KLW9tsN-Uf1GhBONISmicRuZD8ZUZH1ToBjSvnxBwtahNqD7LrcvTmCQn4mRGDtnj8tIdB8BM_dsUab8TyJwpfWgb_9QTCWe8T7IythU8ertOlHnDEVfg-FC-S9XUlNfLuK4UWEb26hfVWkrvjVHNPP_xyWwQAShjRUDSfuX8q0wTlGDNfrqVNrNCNn8lx7MF9WMBW50AxgA"
BOT_TOKEN = "1827610303:AAHWQf7BRUpFaLozN5mIAkVk44xaCB1LBfU"
BOT_NAME = "princess_robot"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@akenoXsupport")
BG_IMAGE =getenv("BG_IMAGE", "https://telegra.ph/file/af1e8f26868716695766e.jpg) 
admins = {}
API_ID = 2742026
API_HASH = "f7a7f2fd4433c4a26355afa93a7e6f85"

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ? !").split())

SUDO_USERS = 1461968113
