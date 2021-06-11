import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQC0XDDR5JXq5HSWkbLzMCsL27429fva-DtyIgO-CWxVfUPjKn4l1CvCosUQvjdycvz6MXelyN_i2v3f8JJ0ZjNaUiIQl-6cDEhCmW0TGHeCI6RSyTpZ3JG8drrxl7Ja_ebKQq7TN8Wo2wlv1oXxm-qVhzmco4vBUM5y_6gXWuOWwELCWlMmIzuPMO-ooow-zONSJqs2hgK-KuBcABAaDWQwiNQjgU_QUKo2cfYbhpMBybKV22Kq81LH-eQWAV9oMUFKtOutvgx9UG695KMrK7nSI-kSmAQ_5L7OfwKKG9KyFsceschjdIkI7G3covbHYbHYYOitjLbbACgsqVejEIV1Q1H2wwA"
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
