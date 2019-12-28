### TRANSACTIONS ###
from helpers import mainnet, testnet
from decimal import Decimal
from pprint import pprint

#We want to send bitcoin to an address
#help(testnet.sendtoaddress()) bitcoin-cli sendtoaddress "1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1
#First send tbtc to your address from a tbtc faucet then eun the program
address = testnet.getnewaddress('','legacy')
address2 = testnet.getnewaddress('','legacy')
print(address)
print(address2)
print(testnet.getbalance())

#We have sent the tbtc to an adress Bize output olarak bir tx döndürdü. We have sent tbtc to ourselves actually. It returned the transaction id
tx = testnet.sendtoaddress(address2, 0.0000100)
print(tx)

#We can get tha transaction and check the input and the outputs
pprint(testnet.gettransaction(tx))