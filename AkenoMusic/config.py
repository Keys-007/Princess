import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQBiMI2SOGkC_dWkdu76mOpE6DHJ7Urwnd-LC2vBESNjo0WukfmA7xVX9nGxjpAUuFJOYCI7YNFU6RJslZHICrzwLIvBorJw6gKBsE2lCgLq8XNr65oYh8wDHr-bHUwyzRxAJFnIKIRyIQq3vaT49l1TLVAaPeyDZFs-R03Uq1cSVhSr46GJBy3ZugBQbafypp8QvHPAmfzcS88qfW950trM6gSRpO2yGBPBM2v_HnZRrvCccAa5peBsmqI5HuNfjJtGBE8acJ8x6E9jLIeLSVHbaJFX_gNIiauW1nLOMz-GfJ_qFed_TenQuYhHmO0Jde-PCckpnRbUg_rOJadgPsAbQ1H2wwA"
BOT_TOKEN = "1700341854:AAGW_H-5wmLJZhmTbru0a0jRs2QfdpbHeTU"
BOT_NAME = "akeno_robot"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@akenoXsupport")
BG_IMAGE =getenv("BG_IMAGE", "https://telegra.ph/file/3cef9662e86bd313ec045.jpg") 
admins = {}
API_ID = 2742026
API_HASH = "f7a7f2fd4433c4a26355afa93a7e6f85"

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ? !").split())

SUDO_USERS = 1461968113
