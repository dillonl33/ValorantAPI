# Valorant API script

# TODO: everything

import requests

URL = "https://api.henrikdev.xyz/valorant/v1/account/dabqu/dabqu"
URL = "https://public-api.tracker.gg/api/v1/{titleSlug}/standard/profile/{platformSlug}/{platformUserIdentifier}"
URL = "https://public-api.tracker.gg/api/v1/valorant/standard/profile/valorant/dabqu#dabqu"
# WORK IN PROGRESS

PARAMS = {'TRN-Api-Key': '9b9207d6-4778-4e6e-8c19-63c7aaa8dcd3'}#'Host': 'public-api.tracker.gg',
#'Accept': 'application/json',
#'Accept-Language': 'en',
#'Accept-Encoding': 'gzip',
#'TRN-Api-Key': '9b9207d6-4778-4e6e-8c19-63c7aaa8dcd3'
#}

r = requests.get(url = URL, params = PARAMS)
print(r)
data = r.json()

print(data) # all data extracted

name = data['data']['name']
account_level = data['data']['account_level']
print('name:', name)
print('level:', account_level)

#"https://public-api.tracker.gg/api/v1/{titleSlug}/standard/profile/{platformSlug}/{platformUserIdentifier}" ,

# 9b9207d6-4778-4e6e-8c19-63c7aaa8dcd3
#GET /v2/<your game>/standard/profile/<platform>/<player identifier>
#Host: public-api.tracker.gg
#Accept: application/json
#Accept-Language: en
#Accept-Encoding: gzip, deflate, br
#TRN-Api-Key: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

