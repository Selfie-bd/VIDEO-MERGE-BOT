import os


class Config(object):
    API_ID = os.environ.get("API_ID", "7434892" )
    API_HASH = os.environ.get("API_HASH", "b645623710413894a1c0e084450876e2" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "video-merger-bot" )
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001576361605" )
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001597887921" )
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "2ab52c1ef915e52f4ee8" )
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "zwgdM4xjXpsYPAP" )
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority" )
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1990460616))

    START_TEXT = """ 
         HELLO 👋 **NAME:** [{cb.from_user.first_name}](tg://user?id={str(cb.from_user.id)})\n**your Username:** `{cb.from_user.username}`\n**your UserID:** `{cb.from_user.id}`\nI am RPLAY ™ Video Merge Bot!\nI can Merge Multiple Videos into One Video.\n Video Formats should be same.\nMade by @renishrplay"
"""
    CAPTION = "Video Merged by @{}\n\nMade by @renishrplay"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
