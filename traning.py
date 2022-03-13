import sys
import requests
import json

client_id = '74f7a56323c7af1bec85'
client_secret = 'f6c3dd3d511bc34e7c38c4c722413c23'
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
head = {'X-Xapp-Token': token}
dict_h = {}
fil = open('dataset_24476_4.txt')
for i in fil:
    res = requests.get(f'https://api.artsy.net/api/artists/{i.strip()}', headers=head)
    js = res.json()
    dict_h[js['sortable_name']] = js['birthday']
print(*[i[0] for i in sorted(dict_h.items(), key=lambda x: (x[1], x[0]))], sep='\n')