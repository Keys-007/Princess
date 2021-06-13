import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQBWdj7KYmEHKaPmAWOvfR222fIklhP3L8DJk0-1vDsEqBX5j7w11d_UHOm3qKI7IKlsuw6uQQ5wmF2YZg1Fdl7NZGIEwPgF6H_CDuu9LqkE3N1OweWOX2LktzTJUzIsXftekyYi3nipgYwnXmGc6gtK2ZztVMkKVmv53rtKv3oVih88-IEqMg0uDt6cxFhmG1etSwv1cWSFgAug3IGd7CyNm8CI0v-rFHHm2zeT5g5don0GJcfoDyw9S1KeFTevpnPavAOReIRsEhEdkwxFKey7vmwM4GCemB8iTWUC_apme9mi1lo61S2KJ1Bc9ECoI7UnZscO-UO2YAc3nbiRkOvdW50AxgA"
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
