import sys
import os

import pytest

sys.path = [os.path.join(os.path.dirname(__file__), "..")] + sys.path
from physt.io.protobuf import to_protobuf
from physt.io.protobuf import from_protobuf
from physt.examples import normal_h1, normal_h2


class TestProtobuf(object):
    def test_h1(self):
        H = normal_h1()
        m = to_protobuf(H)
        H_ = from_protobuf(m)
        assert H_ == H

    def test_h2(self):
        H = normal_h2()
        m = to_protobuf(H)
        H_ = from_protobuf(m)
        assert H_ == H

if __name__ == "__main__":
    pytest.main(__file__)