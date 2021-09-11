from pwn import *
import base64
import time

watch = remote("103.152.242.242", 1457)
toalice = remote("103.152.242.242", 1456)
tobob = remote("103.152.242.242", 1458)
secret = "secret"

g = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
g += 1
g = bytes(g)


def test(g):
    assert g > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def sendAndRet(r, d):
    r.sendline(d)
    print(r.recv(1024))

def sendB64AndRet(r, d):
    r.sendline(base64.b64encode(d))
    print(r.recv())

def inputAndSend(name, r):
    d = input(name+":")
    r.sendline(str(d))

def inputAndSendb64(name, r):
    d = input(name+":")
    r.sendline(base64.b64encode(str(d)))
    
sendB64AndRet(watch, g)
sendB64AndRet(tobob, secret)
sendB64AndRet(tobob, g)
sendB64AndRet(toalice, secret)
sendB64AndRet(toalice, g)

while True:
    inputAndSendb64("tobob", tobob)
    print(tobob.recv())
    print("="*16)

    inputAndSendb64("toalice", toalice)
    print(toalice.recv())
    print("="*32)
    
    time.sleep(0.5)
# test(g)