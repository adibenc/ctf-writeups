import requests as req
import json
from pprint import pprint

url = "http://103.152.242.243:5535/"

expr = "0.1 + 0.2"
r = req.post(url, data={
   "expr": expr
})
print(expr)
pprint(r.content)