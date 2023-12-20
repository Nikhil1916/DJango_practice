import requests
import json
URL = ""

data = {
      'name':'nikhil',
      'roll_no': '2344',
      'city': 'ludhiana'
      }

json_data = json.dumps(data)

r = requests.post(url=URL,data=json_data)

data = r.json()

print(data)