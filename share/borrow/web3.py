from web3 import Web3, Account
import os, json
from django.conf import settings
from web3.middleware import geth_poa_middleware

rpc_url = 'https://data-seed-prebsc-1-s2.bnbchain.org:8545'
web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

def load_contract_abi():
    abi_path = os.path.join(settings.STATICFILES_DIRS[0], 'abi', 'ShareTokenABI.json')
    with open(abi_path, 'r') as file:
        contract_abi = json.load(file)
    return contract_abi

contract_address = '0x27ab1897F2649b84d10AC4cDBcdAed8C3Fb5edB0'
chain_id = '0x61'; #mainnet 0x38 testnet 0x61
abi = load_contract_abi()
contract = web3.eth.contract(address=contract_address, abi=abi)

owner_private_key = settings.PRIVATE_KEY
owner_account = Account.from_key(owner_private_key)

def returnDepositAndAirdrop(borrower_address, contributor_address, depositAmount, damagePercentage, airdropAmount):
    nonce = web3.eth.get_transaction_count(owner_account.address)
    transaction = contract.functions.returnDepositAndAirdrop(borrower_address, contributor_address, depositAmount, damagePercentage, airdropAmount).build_transaction({
        'chainId': chain_id, 
        'gas': 2000000,
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.sign_transaction(transaction, owner_private_key)
    signed_txn_raw = signed_txn.rawTransaction
    txn_hashtxn_hash = web3.eth.send_raw_transaction(signed_txn_raw)
    
    return txn_hashtxn_hash.hex()
    
def borrowerNotPickedUpReturnDeposit(borrower_address, contributor_address, depositAmount) :
    nonce = web3.eth.get_transaction_count(owner_account.address)
    transaction = contract.functions.borrowerNotPickedUpReturnDeposit(borrower_address, contributor_address, depositAmount).build_transaction({
        'chainId': chain_id,  
        'gas': 2000000,
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.sign_transaction(transaction, owner_private_key)
    signed_txn_raw = signed_txn.rawTransaction
    txn_hashtxn_hash = web3.eth.send_raw_transaction(signed_txn_raw)
    
def cancelOrderReturnDeposit(borrower_address, depositAmount) :
    nonce = web3.eth.get_transaction_count(owner_account.address)
    transaction = contract.functions.cancelOrderReturnDeposit(borrower_address, depositAmount).build_transaction({
        'chainId': chain_id, 
        'gas': 2000000,
        'nonce': nonce,
    })
    
    signed_txn = web3.eth.account.sign_transaction(transaction, owner_private_key)
    signed_txn_raw = signed_txn.rawTransaction
    txn_hashtxn_hash = web3.eth.send_raw_transaction(signed_txn_raw)

def get_next_unlock():
    result = contract.functions.nextUnlock().call()
    return {'days': result[0], 'hours': result[1]}

def unlock_tokens():
    nonce = web3.eth.get_transaction_count(owner_account.address)
    transaction = contract.functions.unlockTokens().build_transaction({
        'chainId': int(chain_id, 16), 
        'gas': 2000000,
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(transaction, owner_private_key)
    signed_txn_raw = signed_txn.rawTransaction
    txn_hashtxn_hash = web3.eth.send_raw_transaction(signed_txn_raw)
    return txn_hashtxn_hash.hex()