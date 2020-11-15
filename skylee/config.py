from skylee.sample_config import Config


class Development(Config):
    OWNER_ID =  816157233 # my telegram ID
    OWNER_USERNAME = "doggy_cheems"  # my telegram username
    API_KEY = "1221978373:AAENSOKIr8FXnJ9huhzRrH8idnL4leBq7kc"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://weygupfewpcjls:eff163b09baec6bcac08a06268048ebe1b56064fe9e7bd18ceb502c8127bf37b@ec2-34-204-121-199.compute-1.amazonaws.com:5432/deupr96st7c30i'  # sample db credentials
    MESSAGE_DUMP = '-354482383' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = ff3b1871585d32a794465da51b077361 # for purge stuffs
    TELETHON_ID = 1519291
