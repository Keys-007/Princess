import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "1BVtsOJ4Bu3yEJCoq9OjSxuJ38cxSRNyY_BiMrFhc6j3WGPDcRrrvKnjk08EZ_YfZHB8EKwxm7Mor0GOMXdrcpQlipdTiOPP70aZ_hReyDmIk2TW2cpi-_7XpjjEycC4apC9NOSTlqBlLqJUfI0rPagfR1Efu5Zxvbq6OOwrInD2VPp80Kf8FZgoYpWyGkv0vhQ6MWKUaiMhJ-p1sn-mVX-KEm3F7dQPAeSNT5wzMP4-v8r1igdBaUNcZCZWDj61hqWQ6vIoyPGVwqHzDu34QsPgLf-dNKsZYWyxOtFI3GMozMuK7ELeVGg8y36BFWN0mA_LLwFt5E3e-2wbAmhisI_TH23xclR4="
BOT_TOKEN = "1827610303:AAFQj58Dp8oduTKayyhEbzFoMbhcEcSaBuo"
BOT_NAME = "princess_robot"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@akenoXsupport")
BG_IMAGE =getenv("BG_IMAGE", "https://telegra.ph/file/4867a4913b1d04c663850.jpg") 
admins = {}
API_ID = 2742026
API_HASH = "f7a7f2fd4433c4a26355afa93a7e6f85"

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ? !").split())

SUDO_USERS = 1461968113
