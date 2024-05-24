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

# Function to submit model updates
def submit_update(update_hash):
    tx_hash = contract.functions.submitUpdate(update_hash).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

if __name__ == "__main__":
    # Example submission
    submit_update('hash_of_local_model_1')
