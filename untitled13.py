#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:28:38 2021

@author: yubyeongheon
"""

import requests


BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

end_point = f"{BASE_URL}/start"


headers = {
    "X-Auth-Token": "38c67dd414cf659f28aba28a4401603d",
    "Content-Type": "application/json"
}
body = {
    "problem": 1
}

resp = requests.post(end_point, headers=headers, json=body)
print(resp.status_code, resp.text)
if resp.status_code == 200:
    # API 응답은 성공
    result = resp.json()
    
    _time = result["time"]
elif resp.status_code in (400, 401, 500):
    # 에러니까 알아서 처리
    pass


'''
import json

json_string = '{"a": 1, "b": 2, "c": "aasdasd"}'
json_data = json.load(json_string)
'''

headers = {
    "Authorization": result["auth_key"],
    "Content-Type": "application/json"
}

resp = requests.get(f"{BASE_URL}/locations", headers=headers)
result = resp.json()

locations = result["locations"]

for loc in locations:
    _id = loc["id"]
    located_bikes_count = loc["located_bikes_count"]



command = {
       "commands": [
         { "truck_id": 0, "command": [2, 5, 4, 1, 6] },
         { "truck_id": 1, "command": [2, 5, 4, 1, 6] },
       ]
     }
resp = requests.put(f"{BASE_URL}/simulate", headers=headers, json=command)

result = resp.json()



class APIHandler:
    BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

    def _get(self, path, params=None, headers=None):
        url = f"{BASE_URL}{path}"
        resp = requests.get(url, params=params, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"ERROR!! {resp.text}")
    
    

