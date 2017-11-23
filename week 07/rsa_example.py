# install the rsa package with pip install 
# e.g.
# pip install rsa

import rsa
import binascii

(bob_pub, bob_priv) = rsa.newkeys(512)
message = 'hello Bob!'

crypto = rsa.encrypt(message, bob_pub)
print binascii.hexlify(crypto)

message = rsa.decrypt(crypto, bob_priv)
print message