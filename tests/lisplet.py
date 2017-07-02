def left_op(a, b):
    return Lisplet(a, b)


def right_op(a, b):
    return Lisplet(b, a)


class Lisplet:
    """Removes the incidental mathematics from tests of operator applications. This ensures logic errors won't be
    hidden due to the mathematical properties of integers or rational numbers. It also simplifies test cases because
    we don't have to consider things like division or modulus by zero, and we don't have to come up with useful
    parameters for things with trivial solutions like integer division.

    All operations other than equality and comparison are defined as `op(x, y) -> Lisplet(x, y)`.
    As for equality, two Lisplets are equal if and only if their left and right elements are equal.
    Furthermore, a Lisplet is never equal to a value that is not a Lisplet.
    Comparison of two Lisplets is equivalent to the comparison of their first items.

    Lisplets are callable, returning a Lisplet containing themselves and an `(args, kwargs)` pair.
    They are also indexable and iterable, with `Lisplet(a, b)` acting as the tuple `(a, b)` for these purposes.

    >>> a, b = Lisplet(1), 2

    Equality examples:
    >>> Lisplet(1, 2) == Lisplet(1, 2)
    True
    >>> Lisplet(1, 12) == Lisplet(1, 2)
    False
    >>> Lisplet(12, 2) == Lisplet(1, 2)
    False
    >>> Lisplet(1) == Lisplet(1)
    True
    >>> Lisplet(1) == Lisplet(1, 2)
    False
    >>> Lisplet(1) == Lisplet(2)
    False
    >>> Lisplet() == Lisplet()
    True
    >>> Lisplet() == Lisplet(1, 2)
    False
    >>> Lisplet() == Lisplet(1)
    False

    Comparison examples:
    >>> Lisplet(1, 2) < Lisplet(1, 2)
    False
    >>> Lisplet(1, 2) < Lisplet(12, 2)
    True
    >>> Lisplet(1, 2) > Lisplet(1, 2)
    False
    >>> Lisplet(12, 2) > Lisplet(1, 2)
    True
    >>> Lisplet(1, 2) <= Lisplet(1, 2)
    True
    >>> Lisplet(1, 2) >= Lisplet(1, 2)
    True
    >>> Lisplet(1, 12) < Lisplet(1, 2)
    False
    >>> Lisplet(1, 12) < Lisplet(12, 2)
    True
    >>> Lisplet(1, 12) > Lisplet(1, 2)
    False
    >>> Lisplet(12, 12) > Lisplet(1, 2)
    True
    >>> Lisplet(1, 12) <= Lisplet(1, 2)
    True
    >>> Lisplet(1, 12) >= Lisplet(1, 2)
    True
    >>> Lisplet() < Lisplet()
    False
    >>> Lisplet() <= Lisplet()
    True
    >>> Lisplet() > Lisplet()
    False
    >>> Lisplet() >= Lisplet()
    True

    Sequence operations:
    >>> len(Lisplet())
    0
    >>> len(Lisplet(1))
    1
    >>> len(Lisplet(1, 2))
    2
    >>> Lisplet(12, 24)[0]
    12
    >>> Lisplet(12, 24)[1]
    24
    >>> Lisplet()[0] is None
    True
    >>> Lisplet()[1] is None
    True
    >>> Lisplet(12)[0]
    12
    >>> Lisplet(12)[1] is None
    True
    >>> Lisplet(12, 24)[2]
    Traceback (most recent call last):
        ...
    IndexError: tuple index out of range
    >>> [*Lisplet(1, 2)]
    [1, 2]
    >>> [*Lisplet(1)]
    [1]
    >>> [*Lisplet(None, 2)]
    [2]
    >>> [*Lisplet()]
    []
    >>> [item for item in Lisplet(1, 2)]
    [1, 2]
    >>> [item for item in Lisplet(1)]
    [1]
    >>> [item for item in Lisplet(None, 2)]
    [2]
    >>> [item for item in Lisplet()]
    []

    Call example:
    >>> a('arg1', 'arg2', a='kwarg_a', b='kwarg_b')
    Lisplet(Lisplet(1), (('arg1', 'arg2'), (('a', 'kwarg_a'), ('b', 'kwarg_b'))))

    Left operation examples:
    >>> a + b
    Lisplet(Lisplet(1), 2)
    >>> a - b
    Lisplet(Lisplet(1), 2)
    >>> a * b
    Lisplet(Lisplet(1), 2)
    >>> a @ b
    Lisplet(Lisplet(1), 2)
    >>> a / b
    Lisplet(Lisplet(1), 2)
    >>> a // b
    Lisplet(Lisplet(1), 2)
    >>> a % b
    Lisplet(Lisplet(1), 2)
    >>> a & b
    Lisplet(Lisplet(1), 2)
    >>> a | b
    Lisplet(Lisplet(1), 2)
    >>> a ^ b
    Lisplet(Lisplet(1), 2)
    >>> a << b
    Lisplet(Lisplet(1), 2)
    >>> a >> b
    Lisplet(Lisplet(1), 2)

    Right operation examples:
    >>> b + a
    Lisplet(2, Lisplet(1))
    >>> b - a
    Lisplet(2, Lisplet(1))
    >>> b * a
    Lisplet(2, Lisplet(1))
    >>> b @ a
    Lisplet(2, Lisplet(1))
    >>> b / a
    Lisplet(2, Lisplet(1))
    >>> b // a
    Lisplet(2, Lisplet(1))
    >>> b % a
    Lisplet(2, Lisplet(1))
    >>> b & a
    Lisplet(2, Lisplet(1))
    >>> b | a
    Lisplet(2, Lisplet(1))
    >>> b ^ a
    Lisplet(2, Lisplet(1))
    >>> b << a
    Lisplet(2, Lisplet(1))
    >>> b >> a
    Lisplet(2, Lisplet(1))
    """
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __getitem__(self, item):
        return (self.a, self.b)[item]

    def __iter__(self):
        return iter([item for item in (self.a, self.b) if item is not None])

    def __len__(self):
        return len([item for item in (self.a, self.b) if item is not None])

    __add__ = left_op
    __sub__ = left_op
    __mul__ = left_op
    __matmul__ = left_op
    __floordiv__ = left_op
    __truediv__ = left_op
    __mod__ = left_op
    __and__ = left_op
    __or__ = left_op
    __xor__ = left_op
    __lshift__ = left_op
    __rshift__ = left_op

    __radd__ = right_op
    __rsub__ = right_op
    __rmul__ = right_op
    __rmatmul__ = right_op
    __rfloordiv__ = right_op
    __rtruediv__ = right_op
    __rmod__ = right_op
    __rand__ = right_op
    __ror__ = right_op
    __rxor__ = right_op
    __rlshift__ = right_op
    __rrshift__ = right_op

    def __call__(self, *args, **kwargs):
        # kwargs has to be handled like so because the order of dictionary elements is undefined, which breaks doctests
        # if we just use a dictionary directly.
        return Lisplet(self, (args, tuple(sorted(kwargs.items(), key=lambda k: k[0]))))

    def __eq__(self, other):
        return isinstance(other, Lisplet) and other.a == self.a and other.b == self.b

    def __repr__(self):
        items = (self.a, self.b)[:int(self.b is not None) + 1]

        return '{}({})'.format(type(self).__name__, ', '.join(repr(item) for item in items))

    def __str__(self):
        items = (self.a, self.b)[:int(self.b is not None) + 1]

        return str(items)

    def __lt__(self, other):
        return compare(self.a, other.a) < 0

    def __le__(self, other):
        return compare(self.a, other.a) <= 0

    def __gt__(self, other):
        return compare(self.a, other.a) > 0

    def __ge__(self, other):
        return compare(self.a, other.a) >= 0


def compare(a, b):
    """None-aware comparison helper for Lisplet.

    >>> compare(None, None)
    0
    >>> compare(None, 12)
    -1
    >>> compare(12, None)
    1
    >>> compare(12, 12)
    0
    >>> compare(12, -12)
    1
    >>> compare(-12, 12)
    -1
    """
    if a is None:
        if b is None:
            return 0

        return -1

    if b is None:
        return 1

    if a < b:
        return -1

    if a > b:
        return 1

    return 0
