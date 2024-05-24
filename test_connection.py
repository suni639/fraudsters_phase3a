import requests

try:
    response = requests.get('http://127.0.0.1:7545')
    if response.status_code == 200:
        print("Connection to Ganache is successful!")
    else:
        print(f"Received unexpected status code {response.status_code}")
except requests.ConnectionError:
    print("Failed to connect to Ganache.")
