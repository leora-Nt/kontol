from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "6973446"))
API_HASH = getenv("API_HASH", "d3a6dbd3e466159f7170f6af7fb35ac1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "tdrki_1")
BOT_TOKEN = getenv("BOT_TOKEN","5340569558:AAG68uG4ruKezHp9VlxCMe-aiL86Job5yj0")
BOT_USERNAME = getenv("BOT_USERNAME", "alifajelegbot")
BOT_NAME = getenv("BOT_NAME","Alifa")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCI1YvSGDFmc_8jy_jgvasd_KV9SicZJrJ0ubVfu7Q2_I6y9_CbrrTZhEEXoiyJClP3uirYto0oY9d5cWj04E2C_THe5yzer0YJkuobu0AWlqElyGaBikwl69J_aZgJYukONlv-y8LuryCUNe49R6fR-fj6ybBRNoOHFO5Rr-wZ206uZzPvmitKTooawrwTLh0O2vnUKW-Ff3vQ8xfweAgqYIK-CXrVQv68XtG_PFCyG23UflIeUIh0O5c8nerDQaGbIOcc3JYWaYv-Y0t_jM3e6nTHucnSzhhdj7jANmCHHqhkld24uKoNjS9MMbjjh7SmgLdCbJQ4Y2lHF-M4r1eldQdxzgA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1963422158").split()))
