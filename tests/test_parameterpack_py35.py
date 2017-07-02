from parameterpack import ParameterPack
from .lisplet import Lisplet


def test_right_matmul():
    pack = ParameterPack(Lisplet(1), Lisplet(2), Lisplet(3))
    a, b, c = pack.items

    assert ... @ pack == a @ (b @ c)


def test_matmul():
    pack = ParameterPack(Lisplet(1), Lisplet(2), Lisplet(3))
    a, b, c = pack.items

    assert pack @ ... == (a @ b) @ c
