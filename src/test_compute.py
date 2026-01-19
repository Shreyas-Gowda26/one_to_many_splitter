import pytest

import compute

def test_as_exponent() -> None:
    assert compute.as_exponent('x-1234567890') == 'x⁻¹²³⁴⁵⁶⁷⁸⁹⁰'

def test_as_base_invalid() -> None:
    # base < 2
    with pytest.raises(ValueError):
        compute.as_base(1, 5)

def test_as_base_edge() -> None:
    # num == 0
    empty = compute.as_base(6, 0)
    assert type(empty) is dict
    assert len(empty) == 0

def test_as_base_small() -> None:
    # abs(num) < b
    simple = compute.as_base(4, 3)
    assert type(simple) is dict
    assert simple.items() == {(0, 3)}

def test_as_base_pos() -> None:
    # num >= b
    pos = compute.as_base(3, 32)
    assert type(pos) is dict
    assert pos.items() == {(0, 2), (1, 1), (2, 0), (3, 1)}

def test_as_base_neg() -> None:
    # -num >= b
    neg = compute.as_base(2, -19)
    assert type(neg) is dict
    assert neg.items() == {(0, -1), (1, -1), (2, 0), (3, 0), (4, -1)}
