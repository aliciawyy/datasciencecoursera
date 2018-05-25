from datetime import datetime

from mini_blockchain import base


def test_block_init():
    block = base.Block(0, 0.125, "2018-05-20", "2584a14d")
    assert datetime(2018, 5, 20) == block.timestamp
    expected_hash = ("be3d2b0cb74a78cd6e1e9515e2cd45d68ff3916885499c92e"
                     "107359017c0ebd4")
    assert expected_hash == block.hash
