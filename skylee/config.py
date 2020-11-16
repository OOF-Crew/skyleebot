from skylee.sample_config import Config


class Development(Config):
    OWNER_ID =  816157233 # my telegram ID
    OWNER_USERNAME = "doggy_cheems"  # my telegram username
    API_KEY = "1221978373:AAENSOKIr8FXnJ9huhzRrH8idnL4leBq7kc"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://mcawowehvphzpg:5065c9e95fcaa4d5778f8d83ac331cecd7817b7022ae45f08d6ff8421431329f@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:5432/d9kp79im13flj5'  # sample db credentials
    MESSAGE_DUMP = '-354482383' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = "1037394974" "1343416318"  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = "ff3b1871585d32a794465da51b077361" # for purge stuffs
    TELETHON_ID = "1519291"
