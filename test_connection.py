import requests
import json

payload = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
}

try:
    response = requests.post('http://127.0.0.1:7545', json=payload)
    if response.status_code == 200:
        print("Connection to Ganache is successful!")
        print("Response:", response.json())
    else:
        print(f"Received unexpected status code {response.status_code}")
except requests.ConnectionError:
    print("Failed to connect to Ganache.")
