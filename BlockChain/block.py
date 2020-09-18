import hashlib
import datetime

class Block:
    def __init__(self, prev_hash, data, timestamp):
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def genensis_block():
        return Block('0','Genesis',datetime.datetime.now())

    def get_hash(self):
        binary_hash_data = (str(self.data) + str(self.prev_hash) + str(self.timestamp)).encode()
        inner_hash = hashlib.sha256(binary_hash_data).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
