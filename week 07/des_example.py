# install the pyDes package with pip install 
# e.g.
# pip install pyDes

import pyDes
import binascii

data = "Pleaseencrypt my data"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(data)

print "Encrypted: %r" % binascii.hexlify(d)
print "Decrypted: %r" % k.decrypt(d)

assert k.decrypt(d) == data