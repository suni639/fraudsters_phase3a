import os
import json
import logging
import joblib
import numpy as np
from web3 import Web3

# Set up logging
logging.basicConfig(level=logging.INFO)

def connect_to_blockchain(ganache_url):
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    if not web3.is_connected():
        logging.error("Failed to connect to Ganache.")
        raise ConnectionError("Failed to connect to Ganache.")
    web3.eth.default_account = web3.eth.accounts[0]
    logging.info("Connected to Ganache.")
    return web3

def load_contract(web3, contract_file_path):
    with open(contract_file_path) as f:
        contract_data = json.load(f)
    contract = web3.eth.contract(
        address=contract_data['networks']['5777']['address'],
        abi=contract_data['abi']
    )
    logging.info("Smart contract loaded.")
    return contract

def serialize_model(model_params):
    # Convert numpy arrays to lists for JSON serialization
    for key, value in model_params.items():
        if isinstance(value, np.ndarray):
            model_params[key] = value.tolist()
    return json.dumps(model_params)

def submit_update(contract, parameters, from_address):
    try:
        tx_hash = contract.functions.submitUpdate(parameters).transact({'from': from_address})
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        logging.info(f"Update submitted with parameters: {parameters[:60]}...")  # Log first 60 chars
        return receipt
    except Exception as e:
        logging.error(f"Failed to submit update: {e}")
        raise

if __name__ == "__main__":
    try:
        # Configuration
        ganache_url = "http://127.0.0.1:7545"
        contract_file_path = 'build/contracts/FederatedLearning.json'
        models_dir = 'models/'  # Directory containing the model files
        
        # Connect to blockchain and load contract
        web3 = connect_to_blockchain(ganache_url)
        contract = load_contract(web3, contract_file_path)
        
        # Submit updates for all models in the directory
        for model_file in os.listdir(models_dir):
            if model_file.endswith('.pkl'):
                model_path = os.path.join(models_dir, model_file)
                model_params = joblib.load(model_path)
                parameters = serialize_model(model_params)
                submit_update(contract, parameters, web3.eth.default_account)
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
