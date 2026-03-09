"""Tests for UI module."""
from unittest.mock import patch

from . import ui


class TestExpandAsBase:
    def test_simple(self) -> None:
        result = ui.expand_as_base(6, {(0, 1)})
        assert result == "1"

    def test_complex(self) -> None:
        result = ui.expand_as_base(6, {(0, 1), (1, 2), (2, 3)})
        assert result == "1 + 2\xb76\xb9 + 3\xb76\xb2"

    def test_negative(self) -> None:
        result = ui.expand_as_base(6, [(0, -1), (1, 2), (2, 3)])
        assert result == "-1 + 2\xb76\xb9 + 3\xb76\xb2"

    def test_negative_complex(self) -> None:
        result = ui.expand_as_base(6, [(0, -1), (1, -2), (2, -3)])
        assert result == "-1 - 2\xb76\xb9 - 3\xb76\xb2"

    def test_zero(self) -> None:
        result = ui.expand_as_base(6, {})
        assert result == "0"

class TestGetInt:
    def test_valid_input(self) -> None:
        with patch("builtins.input", return_value="5"):
            result = ui.get_int(lambda n: True)
            assert result == 5

    def test_invalid_then_exit(self) -> None:
        with patch("builtins.input", side_effect=["invalid", "q"]):
            result = ui.get_int(lambda n: True, exit_phrase="q")
            assert result is None

    def test_decimal_then_exit(self) -> None:
        with patch("builtins.input", side_effect=["2.5", "q"]):
            result = ui.get_int(lambda n: True, exit_phrase="q")
            assert result is None

    def test_exit_phrase(self) -> None:
        with patch("builtins.input", return_value="Q"):
            result = ui.get_int(lambda n: True, exit_phrase="Q")
            assert result is None

    def test_valid_condition(self) -> None:
        with patch("builtins.input", return_value="2"):
            result = ui.get_int(lambda n: n > 0)
            assert result == 2

    def test_invalid_condition(self) -> None:
        with patch("builtins.input", side_effect=["-5", "q"]):
            result = ui.get_int(lambda n: n > 0, exit_phrase="q")
            assert result is None

    def test_no_exit_phrase(self) -> None:
        with patch("builtins.input", return_value="42"):
            result = ui.get_int(lambda n: True)
            assert result == 42

    def test_numeric_exit_phrase(self) -> None:
        with patch("builtins.input", return_value="66"):
            result = ui.get_int(lambda n: True, exit_phrase="66")
            assert result is None

    def test_eof(self) -> None:
        with patch("builtins.input", side_effect=EOFError()):
            result = ui.get_int(lambda n: True)
            assert result is None
