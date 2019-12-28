###    Digital Signatures    ###

from helpers import mainnet,testnet
from pprint import pprint

#sign and verify messages like this: signmessage "address" "message"

#First we have to get an address:
address = testnet.getnewaddress('','legacy')
print(f"Address created with private key is:{address}")

#Create our message. Just a basic string
msg = 'this is a message'
print(f"Message is:{msg}")

#Create the signature by signing the address with a message. It returns you a signature
signature = testnet.signmessage(address, msg)
print(f"Signature created with address for the message {msg} is:{signature}")

#Verify that our signature is valid with my address for 'my message' msg
verified = testnet.verifymessage(address, signature, 'this is a message')
print(f"Verified?:{verified}")

#If you try the worng msg to sign, it will print false.
verified2 = testnet.verifymessage(address, signature, 'this is a message too')
print(f"Verified?:{verified2}")