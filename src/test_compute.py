from unittest import TestCase

from . import compute

class TestAsExponent(TestCase):
    def test_general(self) -> None:
        assert compute.as_exponent('x-1234567908') == 'x⁻¹²³⁴⁵⁶⁷⁹⁰⁸'

class TestAsBase(TestCase):
    def test_invalid_base(self) -> None:
        with self.assertRaises(ValueError):
            compute.as_base(1, 5)

    def test_empty(self) -> None:
        empty = compute.as_base(6, 0)
        assert type(empty) is dict
        assert len(empty) == 0

    def test_small_argument(self) -> None:
        simple = compute.as_base(4, 3)
        assert type(simple) is dict
        assert simple.items() == {(0, 3)}

    def test_positive_base(self) -> None:
        pos = compute.as_base(3, 32)
        assert type(pos) is dict
        assert pos.items() == {(0, 2), (1, 1), (2, 0), (3, 1)}

    def test_negative_base(self) -> None:
        neg = compute.as_base(2, -19)
        assert type(neg) is dict
        assert neg.items() == {(0, -1), (1, -1), (2, 0), (3, 0), (4, -1)}
