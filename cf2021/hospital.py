import requests as req
import json
from pprint import pprint

url = "http://103.152.242.243:2869/donate"
qty = 10**-3
qty2 = 10**-4
data = {
   "items" : [
      {
         "id" : 0,
         "quantity" : 10**-2
      },
      {
         "id" : 1,
         "quantity" : qty
      },
      {
         "id" : 2,
         "quantity" : qty
      },
      {
         "id" : 3,
         "quantity" : qty
      },
      {
         "id" : 4,
         "quantity" : qty
      },
    #   {
    #      "id" : 5,
    #      "quantity" : 1
    #   },
   ]
}

headers = {'content-type': 'application/json'}
r = req.post(url, json=data, headers=headers)

pprint(json.loads(r.content))