import secrets
import time
from typing import List
from core.hashing import gen_sha256


class Block:
    def __init__(self, index: int, data: str, previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self) -> str:
        content = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )

        return gen_sha256(content)

    def refresh_hash(self):
        self.hash = self.calc_hash()


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_init_block()

    def create_init_block(self):
        init_block = Block(0, "First(genesis) block", "0")
        self.chain.append(init_block)

    def add_block(self, data: str):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def validate_integrity(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if not secrets.compare_digest(
                current_block.hash, current_block.calc_hash()
            ):
                return False
            if not secrets.compare_digest(
                current_block.previous_hash, previous_block.hash
            ):
                return False
        return True

    def recalculate_hashes(self):
        for block in self.chain:
            block.refresh_hash()

    def add_block_raw(self, block: Block):
        block.previous_hash = self.chain[-1].hash
        self.chain.append(block)
