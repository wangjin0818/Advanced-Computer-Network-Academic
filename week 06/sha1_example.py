# using hashlib
import hashlib

src = 'this is a md5 test.'
m2 = hashlib.sha1()   
m2.update(src)   
print m2.hexdigest()   
