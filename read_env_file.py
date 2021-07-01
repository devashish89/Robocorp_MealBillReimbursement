# +
import os
from dotenv import load_dotenv

load_dotenv('.env')


def get_secret_value(key):
    return os.getenv(key)


get_secret_value('veryfi_username')
