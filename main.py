import requests
import emotes

for emote in emotes.emoteFileName:
    r = requests.get(emotes.baseURL + emotes.emoteFileName[emote])
    if r.status_code != 200:
        print(emote + ' failed')