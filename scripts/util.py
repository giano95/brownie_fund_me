from brownie import accounts, config, network


def get_account():
    if network.show_active() in config["local_blockchain"]:
        return accounts[-1]
    else:
        return accounts.add(config["wallets"]["from_key"])
