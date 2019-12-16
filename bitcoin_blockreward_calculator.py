from helpers import mainnet
from decimal import Decimal

def calculate_bitcoin_cycle_and_block_reward():
    #This little program tells you the bitcoin's cycle count and the bitcoin block reward amount
    initial_subsidy = Decimal(50)
    blocks_per_halvening = 210000
    last_block = mainnet.getblockchaininfo()["blocks"]
    cycle_count = int(last_block/blocks_per_halvening)
    initial_subsidy /= cycle_count*2
    return {"Cycle":cycle_count+1, "Block_reward":initial_subsidy}

if __name__ == "__main__":
    cycle = calculate_bitcoin_cycle_and_block_reward()
    print(f"Bitcoin is in the {cycle.get('Cycle')}. halvening cycle and the block reward is {cycle.get('Block_reward')} ₿ right now.")