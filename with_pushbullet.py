import requests
from requests.structures import CaseInsensitiveDict
from pushbullet import Pushbullet
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pb = Pushbullet(os.environ.get("PUSHBULLET_KEY"))

url = "https://dashboard.honeygain.com/api/v1/contest_winnings"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {}".format(os.environ.get("HONEYGAIN_TOKEN"))

resp = requests.post(url, headers=headers)

if resp.status_code == 200:
    pb.push_note("🐝 HoneyGain", "The script made you earn " + str(resp.json()["data"]["credits"]) + " credits from the honeygain daily reward!")