from email.headerregistry import Address
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.util import get_account
from scripts.deploy_mock import deploy_mocks


def deploy_fund_me():
    account = get_account()

    # we wanna deploy with the price feed eth address if we are on rinkeby chain
    # or use mocks otherwise
    if network.show_active() not in config["local_blockchain"]:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
