import numpy as np
from web3 import Web3
import json

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
web3.eth.defaultAccount = web3.eth.accounts[0]

# Load smart contract
with open('build/contracts/FederatedLearning.json') as f:
    contract_data = json.load(f)
contract = web3.eth.contract(
    address=contract_data['networks']['5777']['address'],
    abi=contract_data['abi']
)

# Function to aggregate model updates
def aggregate_models(contract):
    updates = contract.functions.getUpdates().call()
    model_params = [update[1] for update in updates]
    aggregated_params = np.mean(model_params, axis=0)
    return aggregated_params

if __name__ == "__main__":
    aggregated_params = aggregate_models(contract)
