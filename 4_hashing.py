###    HASHING    ###

from helpers import mainnet,testnet
from pprint import pprint

# Hash functions takes data and gives you a fingerprint.You CANT reverse it

# This is a built in library in python
# To get more information on hashlib: help(hashlib)
import hashlib

# hashlib onjects return a hash obj
msg = b'hello, i am efe'
hash1 = hashlib.sha256(msg)
print(hash1,'\n')

# with digest we get the data in that hash object
hash2 = hashlib.sha256(msg).digest()
print(hash2,'\n')

# with hexdigest we get the hexadecimal data in that hash object
# Hexadecimal(means 16) characters: 0123456789ABCDEF
hash3 = hashlib.sha256(msg).hexdigest()
print(hash3,'\n')

# Example
# Get a string, turn it into bytes and hash it.
msg2 = input('Enter a string:')
print(msg2.encode()) #turns into byte

#You must change msg to the bytes with encode befre hashing
#hash5 = hashlib.sha256(msg2).hexdigest() #fail. 
#print(hash5)

hash4 = hashlib.sha256(msg2.encode()).hexdigest() #get the hash with encoded string
print(hash4)