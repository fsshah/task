import json

import requests
url = "https://reqres.in/api/users"
users_list = []

headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)
res_dict = r.json()

for i in range(1, res_dict['total_pages']+1):
    url = "https://reqres.in/api/users?page="+str(i)
    r = requests.get(url, headers=headers)
    for j in (r.json())['data']:
        users_list.append(j)

print(users_list)
