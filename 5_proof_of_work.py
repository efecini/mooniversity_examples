import hashlib

#Try to find the hash (of a block) which starts with some amount of zeros. We are impersonating the miners acivities here.

def hashed(d, n):
    d += n.to_bytes(4, 'little')
    return hashlib.sha256(d).hexdigest()

data = b'hash of a block'
nonce = 0
zeros_required = 4

while not (hashed(data, nonce)[:zeros_required] == ('0' * zeros_required)):
    print (nonce, hashed(data, nonce))
    nonce +=1

print('Found:',nonce,hashed(data, nonce))