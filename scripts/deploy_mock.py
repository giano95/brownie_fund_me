from brownie import MockV3Aggregator, network
from scripts.util import get_account
from web3 import Web3


DECIMALS = 8
INITIAL_VALUE = 2000


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, INITIAL_VALUE * (10**DECIMALS), {"from": get_account()}
        )
    print("Mocks Deployed!")


def main():
    deploy_mocks()
