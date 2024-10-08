import re
from os import environ, getenv
from Script import script 
import logging

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', "21845036"))
API_HASH = environ.get('API_HASH', "b9787357754c57417854ba8ca0d35129")
BOT_TOKEN = environ.get('BOT_TOKEN', "6425780977:AAH7vpz3-nPN-iMRd_F4M8Iggv87uASmqBQ")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/91146a63860aded52ddce.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/6956255e32d5383952cb6.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b4b20462d805612a2dc73.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5510849897').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002036366565').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ORG:ORG@cluster0.xcsyn7q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#this shortlink working
IMPORT_JK_SITE = environ.get('IMPORT_JK_SITE', 'krownlinks.com')
IMPORT_JK_API = environ.get('IMPORT_JK_API', '2a757fa5b16d56e25a401e1ddd79f17e47b6ff19')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'True')), True)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/qgJFur2luoE3ZjRk/9")
VERIFY2_URL = environ.get('VERIFY2_URL', "gyanilinks.com")
VERIFY2_API = environ.get('VERIFY2_API', "c874c4713e72bd5c5fcb3cc5e1663a0cd6b2a713")

# 👇==============this doesn't work===============👇
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gyanilinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c874c4713e72bd5c5fcb3cc5e1663a0cd6b2a713')
# ☝️==============don't remove this===============☝️

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'krownlinks.com'))
STREAM_API = (environ.get('STREAM_API', '2a757fa5b16d56e25a401e1ddd79f17e47b6ff19'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/qgJFur2luoE3ZjRk'))
STREAM_LINK_MODE = is_enabled((environ.get('STREAM_LINK_MODE', "False")), False)

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002036736520').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/hdlinks4uu')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/hdlinks4uu')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002119311683))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '0')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Streaming
FILE_TO_LINK_LOG = environ.get("FILE_TO_LINK_LOG", "-1002119311683")
FILE_TO_LINK_APPURL = environ.get("FILE_TO_LINK_APPURL", "https://web-z4lgdq3t7kyg.up-de-fra1-k8s-1.apps.run-on-seenode.com")

BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LusiBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Lusifilms'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200")) 

REPO_OWNER = "Developerr"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
