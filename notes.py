print(int('b',16), int('62ba1cd8a',16)) # Prints the hexadecimal representation of the value.
'''
testnet : A small replica of bitcoin for developers to test their app without real money.
We use bitcoin-cli command to communicate with a node. It is a command line utility.
In this course we use >testnet rather than >bitcoin-cli.
/
>testnet help
>mainnet help
Prints all the commands to use in testnet or mainnet
/
>testnet help getblockchaininfo
Gets the help for the related command
/
>testnet getblockchaininfo
Makes the query with the method for the testnet. mainnet for the actual chain
/
>mainnet getmininginfo
Gives the mining info
/
Check how the nodes talk with each other from https://bitcoin.org/en/developer-reference#protocol-versions
This changes from version to version. ipv4 / ipv6 / onion
/
>testnet getwalletinfo
Gives the wallet info
/
>testnet listtransactions
The transactions related to wallet
/
Code to connect to node
If you don't have bitcoinrpc install it with pip:
pip install python-bitcoinrpc
/
Code:
from bitcoinrpc.authproxy import AuthServiceProxy

N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
big_number = 105936749493397165751943248390023977685888340619776708311600296471039819517671

class RPC:

    def __init__(self, uri):
        self.rpc = AuthServiceProxy(uri)

    def __getattr__(self, name):
        """Hack to establish a new AuthServiceProxy every time this is called"""
        return getattr(self.rpc, name)

rpc_template = "http://%s:%s@%s:%s"
mainnet = RPC(rpc_template %
        ('bitcoin', 'python', '68.183.110.103', 8332))
testnet = RPC(rpc_template %
        ('bitcoin', 'python', 'localhost', 18332))
/
pprint : A package to print objects pretty.Especially JSON objects.
from helpers import testnet
from pprint import pprint

pprint(testnet.getblockchaininfo())

'''