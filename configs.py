import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = """
<b>Hey! {} 👋🏻,
I am here to provide unlimited movies to you all . \n\nJust Write the name of your desired movie and you will get it within few seconds. You can add me to your Groups too.</b>
"""
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = """
<b>Hey! {} 👋🏻,
I am here to provide unlimited movies to you all . \n\nJust Write the name of your desired movie and you will get it within few seconds. You can add me to your Groups too.</b>
"""
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "365"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''I am Shizuka Minamoto and I can Provide You Any Movies or Series. Just Write Your Movie or Series Name Correctly.''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''<b>If You have any queries in using this Bot then Contact Bot Owner</b> <b><a href="https://t.me/movies_halt_owner_bot">Bot Owner</a></b>''')
