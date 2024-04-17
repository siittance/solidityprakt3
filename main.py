from web3 import Web3
from web3.middleware import geth_poa_middleware
from info_contract import abi, address_contract

pip3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
pip3.middleware_onion.inject(geth_poa_middleware, layer=0)
contr = pip3.eth.contract(address=address_contract,abi=abi)

print(f"Баланс смарт-контракта: {pip3.eth.get_balance(address_contract)}")
print(f"Баланс 1 аккаунта: {pip3.eth.get_balance('0x6d2D3E1fd119D3CE7d8E8843C81F38C6d2E52F91')}")
print(f"Баланс 2 аккаунта: {pip3.eth.get_balance('0x53DfB66D655083B9BAd758805B2c87D6A2AB28B8')}")
print(f"Баланс 3 аккаунта: {pip3.eth.get_balance('0x57B5C3444421Db346c747c894D630AF40b7aab97')}")
print(f"Баланс 4 аккаунта: {pip3.eth.get_balance('0x26f1dE0Ef3fdCcC09FCb26A93C73f7B681eDBFFB')}")
print(f"Баланс 5 аккаунта: {pip3.eth.get_balance('0x0Aa10fA3d1363cF4684E142c9baD71F2dE946d67')}")
