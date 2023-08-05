import unittest
import asyncio
from time import time
from eth_account import Account
from eth_account.signers.local import LocalAccount

from main import Block, EthRPC

ANVIL_URL = "http://127.0.0.1:8545"
erpc_ws = EthRPC(TEST_WS, 8)
asyncio.run(erpc_ws.start_pool())


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_pool_start(self):
        await erpc_ws.start_pool()

    async def test_block_num(self):
        # await erpc_ws.start_pool()
        t0 = time()
        r1 = asyncio.create_task(erpc_ws.get_block_number())
        r2 = asyncio.create_task(erpc_ws.get_transaction_count("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"))
        r3 = asyncio.create_task(erpc_ws.get_balance("0xA69babEF1cA67A37Ffaf7a485DfFF3382056e78C"))
        r4 = asyncio.create_task(erpc_ws.get_gas_price())
        r5 = asyncio.create_task(erpc_ws.get_block_by_hash("0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae", False))
        r6 = asyncio.create_task(erpc_ws.get_block_by_number(17578346, False))

        print(await r1)
        print(await r2)
        print(await r3)
        print(await r4)
        print(await r5)
        print(await r6)
        print(time() - t0)



    async def test_transaction_count(self):
        r = await erpc_ws.get_transaction_count("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")
        self.assertIsInstance(r, int)

    async def test_wallet_balance(self):
        self.assertIsInstance(await erpc_ws.get_balance("0xA69babEF1cA67A37Ffaf7a485DfFF3382056e78C"), int)

    async def test_gas_price(self):
        self.assertIsInstance(await erpc_ws.get_gas_price(), int)

    async def test_get_block_by_hash(self):
        r = await erpc_ws.get_block_by_hash("0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae", False)
        print(r)

    async def test_get_block_by_number(self):
        r = await erpc_ws.get_block_by_number(17578346, False)
        print(r)

    async def test_eth_call(self):
        tx = {"from" : "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "to": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "value": hex(1),
              "gas": hex(38983301337),
              "type": hex(1)}
        print(await erpc_ws.call(tx))

    def test_send_transaction(self):
        tx = {"from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "to": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "value": hex(1),
              "gas": hex(30000000),
              "type": hex(1)}
        print(erpc_ws.send_transaction(tx))

    def test_get_transaction_receipt(self):
        tx = {"from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "to": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "value": hex(1),
              "gas": hex(30000000),
              "type": hex(1)}
        x = erpc_ws.send_transaction(tx)
        print(erpc_ws.get_transaction_receipt(x))

    def test_send_raw_transaction(self):
        nonce = erpc.get_transaction_count("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")

        tx = {"from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "to": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
              "value": hex(1),
              "gas": hex(40000000),
              "maxFeePerGas": hex(40000000),
              "maxPriorityFeePerGas": "0x0",
              #"gasPrice": hex(20000000),
              "type": hex(2),
              "nonce": hex(nonce),
              "chainId": "0x1"}
        acc = Account.from_key("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
        raw_transaction = acc.signTransaction(tx)
        transaction = erpc.send_raw_transaction(raw_transaction.rawTransaction.hex())
        print(transaction)
        print(erpc.get_transaction_receipt(transaction))

if __name__ == '__main__':
    unittest.main()
