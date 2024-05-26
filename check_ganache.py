from web3 import Web3
import logging

logging.basicConfig(level=logging.INFO)

def connect_to_ganache():
    """
    Connects to the Ganache blockchain.

    Returns:
        web3 (Web3): An instance of the Web3 class connected to Ganache.
    """
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    if not web3.is_connected():
        logging.error("Failed to connect to Ganache.")
        exit()
    return web3

def check_accounts(web3):
    """
    Checks the accounts available in Ganache and their balances.

    Args:
        web3 (Web3): An instance of the Web3 class connected to Ganache.
    """
    accounts = web3.eth.accounts
    if len(accounts) == 0:
        logging.error("No accounts found in Ganache.")
        exit()
    logging.info(f"Accounts: {accounts}")
    for account in accounts:
        balance = web3.eth.get_balance(account)
        logging.info(f"Account {account} balance: {web3.from_wei(balance, 'ether')} ETH")

if __name__ == "__main__":
    web3 = connect_to_ganache()
    check_accounts(web3)
