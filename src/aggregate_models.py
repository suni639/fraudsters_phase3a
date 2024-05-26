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

def deserialize_model(parameters):
    # Convert JSON strings back to dictionaries and ensure numpy arrays are used
    model_params = json.loads(parameters)
    for key, value in model_params.items():
        if isinstance(value, list):  # Assuming all lists should be converted back to np.ndarray
            model_params[key] = np.array(value)
    return model_params

def federated_averaging(models):
    avg_model = {}
    model_keys = models[0].keys()

    for key in model_keys:
        # Filter out None values and ensure values are numeric
        values = [model[key] for model in models if model[key] is not None and isinstance(model[key], (int, float, np.ndarray))]
        if values:
            avg_model[key] = np.mean(values, axis=0)
        else:
            avg_model[key] = None

    # Handling 'coef_' and 'intercept_'
    if 'coef_' in models[0] and 'intercept_' in models[0]:
        coefs = [model['coef_'] for model in models if model['coef_'] is not None]
        intercepts = [model['intercept_'] for model in models if model['intercept_'] is not None]
        avg_model['coef_'] = np.mean(coefs, axis=0)
        avg_model['intercept_'] = np.mean(intercepts, axis=0)
    else:
        logging.error("Models do not contain 'coef_' and 'intercept_'")
    
    return avg_model

if __name__ == "__main__":
    try:
        # Configuration
        ganache_url = "http://127.0.0.1:7545"
        contract_file_path = 'build/contracts/FederatedLearning.json'
        
        # Connect to blockchain and load contract
        web3 = connect_to_blockchain(ganache_url)
        contract = load_contract(web3, contract_file_path)
        
        # Fetch model parameters from blockchain
        updates_count = contract.functions.getUpdatesCount().call()
        logging.info(f"Number of updates to fetch: {updates_count}")
        
        models = []
        for i in range(updates_count):
            try:
                _, parameters = contract.functions.getUpdate(i).call()
                model_params = deserialize_model(parameters)
                models.append(model_params)
                logging.info(f"Fetched and deserialized update {i+1}/{updates_count}")
                logging.info(f"Model parameters: {model_params}")
            except Exception as e:
                logging.error(f"Failed to fetch or deserialize update {i+1}: {e}")
        
        # Perform federated averaging
        aggregated_model_params = federated_averaging(models)
        logging.info("Federated averaging completed.")
        
        # Ensure 'coef_' and 'intercept_' are included
        if 'coef_' not in aggregated_model_params or 'intercept_' not in aggregated_model_params:
            logging.error("Aggregated parameters do not contain 'coef_' and 'intercept_'")
            raise ValueError("Aggregated parameters do not contain 'coef_' and 'intercept_'")
        
        # Save aggregated model parameters
        joblib.dump(aggregated_model_params, "aggregated_model.pkl")
        logging.info("Aggregated model saved as aggregated_model.pkl")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
