# eth_rpc
### A lightweight Ethereum RPC library for Python

Features include:
- Ability to initiate remote procedure calls on a wide variety of ethereum functions
  - More functions are added whenever possible to this list
- Typed function outputs for easy manipulation of results
- "eth_subscribe" functionality
- Websocket pooling for high performance calls
- Support for RPC batching, allowing multiple calls to the same function at once

### Implemented methods

  - [x] `eth_blockNumber`
  - [x] `eth_getTransactionCount`
  - [x] `eth_getBalance`
  - [x] `eth_gasPrice`
  - [x] `eth_getBlockByNumber`
  - [x] `eth_getblockByHash`
  - [x] `eth_call`
  - [x] `eth_getTransactionReceipt`
  - [x] `eth_sendRawTransaction`
  - [x] `eth_sendTransaction`
  - [x] `eth_syncing`
  - [x] `eth_coinbase`
  - [x] `eth_chainId`
  - [x] `eth_mining`
  - [x] `eth_hashrate`
  - [x] `eth_accounts`
  - [x] `eth_subscribe`

Methods to implement
  - [ ] `eth_getStorageAt`
  - [ ] `eth_getTransactionCountByHash`
  - [ ] `eth_getTransactionCountByNumber`
  - [ ] `eth_getUncleCountByBlockHash`
  - [ ] `eth_getUncleCountByBlockNumber`
  - etc., aiming to complete all methods listed [here.](https://ethereum.org/en/developers/docs/apis/json-rpc/)



### Example usage

#### Basic single function call

```python
# Example usage
import asyncio
from eth_rpc.rpc import EthRPC

TEST_URL = "http://127.0.0.1:8545"
erpc = EthRPC(TEST_URL, pool_size=2)

async def test_transaction_count():
    # Optional step to start your thread pool before your RPC call
    await erpc.start_pool()
    # Gets the number of transactions sent from a given EOA address
    r = await erpc.get_transaction_count("0xabcdefghijklmnopqrstuvwxyz1234567890")
    print(r)
    # Ensures no hanging connections are left
    await erpc.close_pool()

if __name__ == "__main__":
    asyncio.run(test_transaction_count())
```

#### Example subscription

```python
# Example subscription
import asyncio
from eth_rpc.rpc import EthRPC, SubscriptionType

TEST_URL = "http://127.0.0.1:8545"
erpc = EthRPC(TEST_URL, pool_size=2)

async def test_subscription(subscription_type: SubscriptionType):
    """
    Creates a subscription to receive data about all new heads
    Prints each new subscription result as it is received
    """
    async with erpc.subscribe(subscription_type) as sc:
        # The following will iterate as each item is gotten by sc.recv()
        async for item in sc.recv():
            # 'item' is formatted into the appropriate form for its subscription type
            # this is done by the sc.recv() automatically
            print(item)

if __name__ == "__main__":
    asyncio.run(test_subscription(SubscriptionType.new_heads))
```

More examples available in the [demo](https://github.com/gabedonnan/eth_rpc/tree/main/demo) folder.

# Getting started

## Poetry

This project and its dependencies are managed by python poetry,
which will automatically manage the versions of each library / python version
upon which this project depends.

Install poetry with the instructions [here.](https://python-poetry.org/docs/)

## Testing your programs

Testing a program built with this library can be done with actual ethereum
nodes, though they may rate limit you or cost eth to run.
As such using testing programs such as Anvil from the Foundry suite of products
allows for faster and more productive testing.

### Install foundry

Instructions available at [this link.](https://book.getfoundry.sh/getting-started/installation)

### Run anvil

Anvil is a blockchain testing application included with foundry.

The following command will run an instance of anvil representing 
the blockchain's status at block number ```EXAMPLE_BLOCK_NUM``` via url
```EXAMPLE_RPC_URL```.

This is helpful for ensuring consistency in tests.

```bash
anvil rpc-url EXAMPLE_RPC_URL@EXAMPLE_BLOCK_NUM
```

### Acknowledgements

Special thanks to [@totlsota](https://github.com/totlsota) as a more experienced blockchain developer than I, for giving me pointers when I needed them and
generally assisting in the development of this project.
