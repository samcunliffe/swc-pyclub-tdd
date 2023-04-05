import pytest
from roman import to_roman


@pytest.mark.parametrize(
    "arabic_input, expected_roman_output",
    [(1, "I"), (2, "II"), (4, "IV"), (5, "V"), (8, "VIII"), (9, "IX"), (10, "X")],
)
def test_reasonable_input(arabic_input: int, expected_roman_output: str) -> None:
    assert to_roman(arabic_input) == expected_roman_output


@pytest.mark.parametrize(
    "out_of_bounds",
    [0, -1, -100, 4000, 4001, 1e6],  # Roman numerals only exist for 1 → 3999
)
def test_unreasonable_input(out_of_bounds: int) -> None:
    with pytest.raises(ValueError):
        to_roman(out_of_bounds)
