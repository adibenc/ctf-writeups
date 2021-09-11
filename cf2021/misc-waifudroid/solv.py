import binascii as ba

pl = "gimme secret"
pl = ba.hexlify(pl.encode("utf-8"))
# pl = ba.hexlify(pl)
a = str(pl)
print(a)
print(bytes.fromhex("67696d6d6520736563726574"))