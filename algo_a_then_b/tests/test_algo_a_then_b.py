import pytest

from algo_a_then_b.main import main as a_then_b


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("aaaa", True),
        ("a", True),
        ("b", True),
        ("ba", False),
        ("ab", True),
        ("aaab", True),
        ("aaaba", False),
        ("abab", False),
        ("aba", False),
        ("bbbbbbbbbb", True),
        ("bbbbbbbbab", False),
        ('a' * 300_000, True),
        ('a' * 299_999 + 'b', True),
        ('a' * 299_998 + 'ba', False)
    ],
    ids=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] # pytest win32 KI
)
def test_a_then_b(input_string: str, expected_result: list[bool]) -> None:
    assert a_then_b(input_string) == expected_result
