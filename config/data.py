from dotenv import load_dotenv
import os


load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    ZIP_CODE = os.getenv("ZIP_CODE")