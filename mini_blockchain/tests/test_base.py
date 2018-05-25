from unittest import TestCase
from datetime import datetime
import mock

from mini_blockchain import base


class BlockTest(TestCase):
    def setUp(self):
        patcher = mock.patch(
            base.__name__ + ".datetime.now",
            return_value=datetime(2018, 5, 20)
        )
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_block_init(self):
        block = base.Block(0, 0.125, "2584a14d")
        expected_hash = ("be3d2b0cb74a78cd6e1e9515e2cd45d68ff391688"
                         "5499c92e107359017c0ebd4")
        assert expected_hash == block.hash
