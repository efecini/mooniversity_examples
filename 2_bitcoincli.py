from helpers import mainnet,testnet
from pprint import pprint

#If you have a node that is running, you can use a terminal utility to access it by bitcoin-cli

##Get the possible functions or the queries through your node.
#print(testnet.help())

##Get the info for the getblockchaininfo query
#pprint(testnet.help('getblockchaininfo'))

#Get blockchain info 
#pprint(testnet.getblockchaininfo())

#Get mining info 
#pprint(testnet.getmininginfo())

#Get network info
#pprint(testnet.getnetworkinfo())

#Generate a new adress. Testnet adresses start with m or n
#pprint(testnet.getnewaddress("", "legacy"))

#Get the block information. Arg: blockhash and verbosity(This changes the amount of information that it is giving)
#pprint(mainnet.getblock('000000000000000000155040ef7c75f609ee9fdaaabf97a6018d69fca35e6084'))
#pprint(mainnet.getblock('000000000000000000155040ef7c75f609ee9fdaaabf97a6018d69fca35e6084', 0))
#content = str(mainnet.getblock('000000000000000000155040ef7c75f609ee9fdaaabf97a6018d69fca35e6084', 1))
#pprint(mainnet.getblock('000000000000000000155040ef7c75f609ee9fdaaabf97a6018d69fca35e6084', 2))

#put the information to a new txt file
#f = open("new.txt","w")
#f.write(content)
#f.close()