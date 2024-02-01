#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6543814392:AAG__T4oTlbD_IBLLFCuhapy2Mu2rJFb4kk")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "17432758"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "6543814392:AAG__T4oTlbD_IBLLFCuhapy2Mu2rJFb4kk")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQEKALYAxng97RHQrZ3RaphxYoRIkgy1QZgARqsxkvZcRP0xkvOWQuRxucjIKtyBZ4-K9UQg8GghqwqsLlfTNDR1orqbrEklIn0hnY6s1Ufh1auaf5e76M9h1vbQPOzfm09Uu0Cs-dOemRsimRl1csxIDPU2kb5HHFYct75HP0r4Sb9sARvwW1XbZ2aiLP3-E9eXM8Ja4c-k9T7sn942lwIT-JQXPXN_XjcWH3j_rTiiYAO6uXDwcEJBt7jnBLJ47G9EMbLDOZwBwvfEFktSOEUrN5njl5dkJJbnB7iITu5y40Q0JavJclvlVh7M6IAwyIiCk2qa7Rg5G678Q4btCNZZeE3EnwAAAAFrzjAbAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://firozshamuhammad12:1qazmlp0@cluster0.ztqpqro.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
