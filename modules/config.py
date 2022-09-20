import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID","9285707"))
API_HASH = getenv("API_HASH","89615ee7fd66ed4ffc07abcaa454bd20")
BOT_TOKEN = getenv("BOT_TOKEN","5634586617:AAHWJ1OI0IXQqvKPbPiQQgZHVbN_5t3q2Dc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION","AQB1qR6xMItjRFykWexIwG6RmKfU82xBCBaXtP12um_oPrmMccNWGj8935wO9eBWQCHC8bEhamjNBxeodSMhc8uvD2lOYkaEI1jbzBTmNwRRBFliRq96Ecc0w3ETPvCSnMoh0c11Yz0vPz3EZdJ9uELWP2QPqkE07lwCtK8bMySqjCq8LPCbh0LnDA8JYICVmuRnnrgEcB-YJqWjHSjpefNqa0xSAU4kcXBQYAo6WcbNaiKOfKu0xs20JXG4gsQ5A47yyZ-Y1eQtYqkI2d5RSg9R4qXrbbdyKKUx1cjGugiWteWIXNa01whK5ejAdobrG6VgAvpC82ye5dQ2cR1P0hA_AAAAAUap3JQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5414162824").split()))
aiohttpsession = aiohttp.ClientSession()
