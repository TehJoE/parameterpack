Parameter Pack
--------------

.. start-badges
.. image:: https://img.shields.io/pypi/v/parameterpack.svg
    :target: https://pypi.python.org/pypi/parameterpack
.. image:: https://img.shields.io/pypi/pyversions/parameterpack.svg
    :target: https://pypi.python.org/pypi/parameterpack
.. image:: https://img.shields.io/github/release/TehJoE/parameterpack.svg
    :target: https://github.com/TehJoE/parameterpack/releases/latest
.. image:: https://img.shields.io/github/license/TehJoE/parameterpack.svg
    :target: https://github.com/TehJoE/parameterpack/blob/master/LICENSE
.. end-badges

This module provides a mechanism for writing something similar to C++17's `fold expressions`_ in Python. This is
achieved by co-opting Python's mostly unused ``Ellipsis`` literal.


Supported Operators
-------------------

 - Addition (``+``)
 - Subtraction (``-``)
 - Multiplication (``*``)
 - Integer division (``//``)
 - Division (``/``)
 - Modulus (``%``)
 - Matrix Multiplication (``@``, Python >= 3.5 only)
 - Bitwise And (``&``)
 - Bitwise Or (``|``)
 - Bitwise Xor (``^``)
 - Left Shift (``<<``)
 - Right Shift (``>>``)
 - ``__call__``
 - Comparison operators (``>``, ``>=``, ``<``, ``<=``, ``==``, ``!=``)


Examples
--------

There are two ways to "fold" an operation over a parameter pack: *left* and *right* folds.

.. code-block:: python

    from parameterpack import pack

    p = pack(1, 2, 3)

    # Left fold
    p - ...      # (1 - 2) - 3 = -4
    p - ... - 4  # ((1 - 2) - 3) - 4 = -8

    # Right fold
    ... - p     # 1 - (2 - 3) = 2
    ... - p - 4 # 4 - (1 - (2 - 3)) = -2

Note that the left fold groups operations on the left, while the right fold groups them on the right. This only makes
a difference if the folded operation is not associative, such as in the case of integer subtraction.

Because it is not possible to redefine the ``ellipsis`` type's operators, a right fold on the right side of a binary
operation requires parentheses.

.. code-block:: python

    from parameterpack import pack

    p = pack(1, 2, 3)

    # This is an error because "4 - ..." is evaluated first.
    4 - ... - p

    # This is what you should do instead.
    4 - (... - p)  # 4 - (3 - (2 - 1)) = 2

You may prefer to use parentheses in every case to keep the syntax clear and avoid this potential oversight.

Conditional chains are also supported, but they work a little differently from the other folds.

.. code-block:: python

    from parameterpack import pack

    p = pack(1, 2, 3)

    # Python evaluates "a < b < c" as "a < b and b < c", so this module does the same.
    p < ...      # 1 < 2 < 3 = True, so 3 is returned.
    p < ... < 4  # 1 < 2 < 3 < 4 = True
    p < ... < 0  # 1 < 2 < 3 < 0 = False

    p = pack(3, 2, 1)

    p < ...  # 3 < 2 < 1 = False, so a special False-comparing object is returned.
    ... < p  # 3 > 2 > 1 = True

Because python has no reversed-argument forms for the comparison operators, conditionals work a little differently.
If folding the comparison over the parameter pack's elements results in ``False``, in order to invalidate the entire
comparison chain, it will return a special object that will return ``False`` for any further comparisons. Otherwise, the
last element of the parameter pack is returned so that the comparison chain can continue.


Running Tests
-------------

To run this module's tests in your system's Python interpreter, simply run ``python setup.py test`` from the
repository root.

To run tests in all supported interpreters, first ensure that every supported Python interpreter is installed on your
system and added to the `PATH` environment variable. Then run ``pip install -e .[dev]`` from the repository root to
install development dependencies, and then run ``tox`` from the repository root to run the tests.


Bugs Reports and Feature Requests
---------------------------------

Please use the `issue tracker`_ to submit bugs or request features.


License
-------

Copyright Joe Lawson, 2017.

This package is distributed under the terms of the `MIT`_ license.

.. _`MIT`: https://github.com/TehJoE/parameterpack/blob/master/LICENSE
.. _`fold expressions`: http://en.cppreference.com/w/cpp/language/fold
.. _`issue tracker`: https://github.com/TehJoE/parameterpack/issues
