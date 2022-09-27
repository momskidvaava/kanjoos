import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "1480988"))
API_HASH = getenv("API_HASH", "be76b2fd25b50222b0e1eee141d6a259")
BOT_TOKEN = getenv("BOT_TOKEN", "5521157144:AAFyvM59z4_v9yy7bBu0dSIspp6PYwZlG6s")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQByDD7NLDtkWIKAISif2It1SkXmnNxVDLhgq51wICzb_WZPpOa8YEJRQDD1w-VLNTgLkNW7gaLkm7BAV1KkFj_4Cr_9NSzXZHQjjGaUwHbxgRoqbVHe4sDFQMYbUa3AXHn4oktctVqCx-Kbt36eP1GIzOmFcphodHDoWy3CvD4kTlRvCheffcKv1_Ff7yVKjIWqcnhaoPyEEftAjUxH2-1q5_ZWV0rgY_gAt-7AGoSHIcHZ1RWOyccoHu4p3G743i5mNuQU89E2jd0jydFLRynkHWC5OdwJplybPYRdr7U9gWBXfRT9yDfxZ2Z-2I6npPQZJrtHABFP7mFt21_F9YQhAAAAAUp_RwIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5759765152 5616310867 5325376827 2131905308 5715063431 5088486752").split()))
aiohttpsession = aiohttp.ClientSession()
