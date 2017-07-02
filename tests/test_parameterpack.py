import pytest

from parameterpack import ParameterPack
from .lisplet import Lisplet


@pytest.fixture
def pack():
    return ParameterPack(Lisplet(1), Lisplet(2), Lisplet(3))


def test_add(pack):
    a, b, c = pack.items

    assert pack + ... == (a + b) + c


def test_sub(pack):
    a, b, c = pack.items

    assert pack - ... == (a - b) - c


def test_mul(pack):
    a, b, c = pack.items

    assert pack * ... == (a * b) * c


def test_truediv(pack):
    a, b, c = pack.items

    assert pack / ... == (a / b) / c


def test_floordiv(pack):
    a, b, c = pack.items

    assert pack // ... == (a // b) // c


def test_mod(pack):
    a, b, c = pack.items

    assert pack % ... == (a % b) % c


def test_and(pack):
    a, b, c = pack.items

    assert pack & ... == (a & b) & c


def test_or(pack):
    a, b, c = pack.items

    assert pack | ... == (a | b) | c


def test_xor(pack):
    a, b, c = pack.items

    assert pack ^ ... == (a ^ b) ^ c


def test_lshift(pack):
    a, b, c = pack.items

    assert pack << ... == (a << b) << c


def test_rshift(pack):
    a, b, c = pack.items

    assert pack >> ... == (a >> b) >> c


def test_lt(pack):
    a, b, c = pack.items

    assert bool(pack < ...) == bool(a < b < c)


def test_le(pack):
    a, b, c = pack.items

    assert bool(pack <= ...) == bool(a <= b <= c)


def test_gt(pack):
    a, b, c = pack.items

    assert bool(pack > ...) == bool(a > b > c)


def test_ge(pack):
    a, b, c = pack.items

    assert bool(pack >= ...) == bool(a >= b >= c)


def test_eq():
    pack = ParameterPack(1, 1, 1)
    assert (pack == ...) == 1
    assert not (pack == ...) == 0
    assert not (ParameterPack(1, 0, 1) == ...) == 1


def test_ne():
    """This one may seem a little counter-intuitive, but the intuitive interpretation is inconsistent.
    All comparison operations are evaluated as
    (x[0] op x[1]) and (x[1] op x[2]) and ... (x[n-1] op x[n]) and (x[n] op other)
    which means that the __ne__ operation is always false if two consecutive items in the
    ParameterPack are equal.
    """
    pack = ParameterPack(1, 1, 1)

    assert not (pack != ...) != 2
    assert not (pack != ...) != 1
    assert not (ParameterPack(1, 0, 1) != ...) != 1

    pack = ParameterPack(1, 2, 3)
    assert (pack != ...) != 1
    assert (pack != ...) != 2
    assert not (pack != ...) != 3


def test_right_add(pack):
    a, b, c = pack.items

    assert ... + pack == a + (b + c)


def test_right_sub(pack):
    a, b, c = pack.items

    assert ... - pack == a - (b - c)


def test_right_mul(pack):
    a, b, c = pack.items

    assert ... * pack == a * (b * c)


def test_right_truediv(pack):
    a, b, c = pack.items

    assert ... / pack == a / (b / c)


def test_right_floordiv(pack):
    a, b, c = pack.items

    assert ... // pack == a // (b // c)


def test_right_mod(pack):
    a, b, c = pack.items

    # Ensure we don't get a 0 result at any point.
    if b % c == 0:
        b += 1
    if a % (b % c) == 0:
        a += 1

    pack = ParameterPack(a, b, c)

    assert ... % pack == a % (b % c)


def test_right_and(pack):
    a, b, c = pack.items

    assert ... & pack == a & (b & c)


def test_right_or(pack):
    a, b, c = pack.items

    assert ... | pack == a | (b | c)


def test_right_xor(pack):
    a, b, c = pack.items

    assert ... ^ pack == a ^ (b ^ c)


def test_right_lshift(pack):
    a, b, c = pack.items

    assert ... << pack == a << (b << c)


def test_right_rshift(pack):
    a, b, c = pack.items

    assert ... >> pack == a >> (b >> c)


def test_right_lt(pack):
    a, b, c = pack.items

    assert bool(... < pack) == bool(a > b > c)


def test_right_le(pack):
    a, b, c = pack.items

    assert bool(... <= pack) == bool(a >= b >= c)


def test_right_gt(pack):
    a, b, c = pack.items

    assert bool(... > pack) == bool(a < b < c)


def test_right_ge(pack):
    a, b, c = pack.items

    assert bool(... >= pack) == bool(a <= b <= c)


def test_call(pack):
    a, b, c = pack.items

    assert pack(...) == a(b)(c)
    assert pack(12, ..., 15, extra='kwargs') == a(12, b, 15, extra='kwargs')(12, c, 15, extra='kwargs')


def test_unpack(pack):
    assert ParameterPack(*pack).items == pack.items

