import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "1480988"))
API_HASH = getenv("API_HASH", "be76b2fd25b50222b0e1eee141d6a259")
BOT_TOKEN = getenv("BOT_TOKEN", "5605728947:AAEjB8dhSMGdQMLVqGbYyxxM6DnCQnmTsAE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQCWPW7925QnJEl7uo5rBnnzctHuZwl0X6XkBb2rbhaguA-JV01tqhA0rA50NAporQGP_9Cd5Vx6Bz7CvVjUYhZ6LORkZ86YtnTAJhbPxrfUBeEBKCyoHvUYMV9C2DXDYOS6EXNB918yzJB7nhTWxy_NhYzsB24CRD5pIcX0FV7tmBEpDPeCMCAixGBFYdu0ffWPiFYYP6ozY2J94Rc_vyh9bycBgKiQ8ldOtHsBlAhrxyinq0Y9PbNZpENCXtqjHNbcGDDWW0jUrRSSKnOSa7G2D7o1j8NUlF0FAwo_tgLFblehBippHC5pxS7oiU21WKOVuqraVrNnOCVmItNftP6nAAAAAUp_RwIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5414162824").split()))
aiohttpsession = aiohttp.ClientSession()
