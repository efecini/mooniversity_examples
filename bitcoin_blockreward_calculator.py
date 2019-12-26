from helpers import mainnet
from decimal import Decimal

def calculate_bitcoin_cycle_and_block_reward():
    #This little program gives the bitcoin's cycle count and the bitcoin block reward amount
    INITIAL_SUBSIDY = Decimal(50)
    BLOCKS_PER_HALVENING = 210000
    last_block = mainnet.getblockchaininfo()["blocks"]
    cycle_count = int(last_block/BLOCKS_PER_HALVENING)
    block_reward = INITIAL_SUBSIDY / cycle_count*2
    return {"Cycle":cycle_count+1, "Block_reward":block_reward}

if __name__ == "__main__":
    cycle = calculate_bitcoin_cycle_and_block_reward()
    print(f"Bitcoin is in the {cycle.get('Cycle')}. halvening cycle and the block reward is {cycle.get('Block_reward')} ₿ right now.")