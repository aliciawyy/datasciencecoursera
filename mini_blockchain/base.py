import hashlib
from datetime import datetime

import sheepts


def get_hash_hex(*args):
    sha = hashlib.sha256()
    info = "".join(map(str, args)).encode('utf-8')
    sha.update(info)
    return sha.hexdigest()


class Block(sheepts.StringMixin):
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = datetime.now()
        self.previous_hash = previous_hash
        self.hash = self._get_hash()

    def _get_hash(self):
        return get_hash_hex(
            self.index, self.data, self.timestamp, self.previous_hash
        )


class GenesisBlock(Block):
    def __init__(self, data):
        super(GenesisBlock, self).__init__(0, data, "0")
