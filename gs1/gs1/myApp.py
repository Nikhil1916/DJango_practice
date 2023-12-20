#third party application example
import requests 
URL = 'http://127.0.0.1:8000/studentInfo'

r = requests.get(url = URL)

json = r.json()

print(json)