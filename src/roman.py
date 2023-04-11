def to_roman(arabic: int) -> str:
    if arabic not in range(1, 4000):
        raise ValueError("Roman numerals only map to [1, 3999].")
    numeral = ""
    magic_numbers = [10, 9, 5, 4, 1]
    letters = ["X", "IX", "V", "IV", "I"]
    for n, l in zip(magic_numbers, letters):
        count = arabic // n
        arabic -= count * n
        numeral += count * l
    return numeral
