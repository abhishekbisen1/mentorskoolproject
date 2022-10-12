import hashlib

def md5hash ( private_key,ts,public_key):
    strhash = ts+private_key+public_key
    result  = hashlib.md5(strhash.encode())
    return result.hexdigest(
    ) 

