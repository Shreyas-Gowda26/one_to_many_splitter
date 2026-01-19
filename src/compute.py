import math
from typing import Dict

import shims

_EXP_DIGITS = {
    '0': '\u2070',
    '1': '\xb9',
    '2': '\xb2',
    '3': '\xb3',
    '4': '\u2074',
    '5': '\u2075',
    '6': '\u2076',
    '7': '\u2077',
    '8': '\u2078',
    '9': '\u2079',
    '-': '\u207b',
}

def as_base(b: int, num: int) -> Dict[int, int]:
    '''
    Outputs a dictionary mapping exponents to scalars,
    which describe `num` as a base `b` number.
    Throws a `ValueError` if the inputs are invalid.

    Example usage:

    ```
    #b, num = ...
    exp_scalars = as_base(b, num)
    sum(s * b ** i for i, s in exp_scalars.items()) == num # True
    ```

    :param b: The base. Must be at least 2.
    :type b: int
    :param num: The number to represent in base `b`
    :type num: int
    :return: A dictionary of exponent-to-scalar mappings.
    An empty dictionary if `num` is 0.
    :rtype: Dict[int, int]
    '''
    tmp_num = abs(num)
    if b < 2:
        raise ValueError(f'The logarithm of base {b} is potentially complex-valued or indeterminate')
    elif tmp_num == 0:
        return {}
    elif tmp_num < b:
        return {0: num}
    out: Dict[int, int] = {}
    i = 0
    while tmp_num != 1:
        tmp_num, mod = shims.divmod(tmp_num, b)
        out[i] = int(math.copysign(mod, num))
        i += 1
    out[i] = int(math.copysign(1, num))
    return out

def as_exponent(n: int | str) -> str:
    '''
    Stringifies `n` as superscript digits

    :param n: The number
    :type n: int | str
    :return: The number in superscript
    :rtype: str
    '''
    return ''.join(_EXP_DIGITS.get(c, c) for c in str(n))
