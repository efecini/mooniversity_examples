from helpers import mainnet, testnet
from decimal import Decimal
from pprint import pprint

def calculate_bitcoin_cycle_and_block_reward():
    #This little program gives the bitcoin's cycle count and the bitcoin block reward amount
    INITIAL_SUBSIDY = 50
    BLOCKS_PER_HALVENING = 210000
    last_block = mainnet.getblockchaininfo()["blocks"]
    cycle_count = int(last_block/BLOCKS_PER_HALVENING)
    block_reward = INITIAL_SUBSIDY / (cycle_count*2)
    return cycle_count+1, block_reward

if __name__ == "__main__":
    cycle, block_reward = calculate_bitcoin_cycle_and_block_reward()
    pprint(cycle)
    print(f"Bitcoin is in the {cycle}. halvening cycle and the block reward is {block_reward} ₿ right now.")