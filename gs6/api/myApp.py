import requests
import json
URL = ""

def get_data(id = None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    json_data = json.dumps(data)    
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# getData(2)

def postData():
    data = {
        'name': 'Ravi',
        'roll_no': 34,
        'city': 'dhanbad'
    }      
    
    URL = ""
    
    json_data = json.dumps(data)
    
    r = requests.post(url=URL, data=json_data)
    
    print(r.json())