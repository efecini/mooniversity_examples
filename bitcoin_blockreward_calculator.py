from helpers import mainnet
from decimal import Decimal

#This little program tells you the bitcoin's cycle count and the bitcoin block reward amount

initial_subsidy = Decimal(50)
blocks_per_halvening = 210000
last_block = mainnet.getblockchaininfo()["blocks"]
cycle = int(last_block/blocks_per_halvening)
initial_subsidy /= cycle*2

print(f"Bitcoin is in the {cycle+1}. halvening cycle and the block reward is {initial_subsidy} btc right now.")