def to_roman(arabic: int) -> str:
    """Convert an Arabic numeral to Roman numeral."""
    numeral = ""
    ints = [10, 9, 5, 4, 1]
    roms = ["X", "IX", "V", "IV", "I"]
    for i, r in zip(ints, roms):
        count = arabic // i
        numeral += r * count
        arabic -= i * count
    return numeral


def to_roman_(arabic: int) -> str:
    numeral = ""
    while arabic >= 10:
        arabic -= 10
        numeral += "X"

    if arabic == 9:
        arabic -= 9
        numeral += "IX"

    if arabic >= 5:
        arabic -= 5
        numeral += "V"

    if arabic == 4:
        arabic -= 4
        numeral += "IV"

    while arabic > 0:
        arabic -= 1
        numeral += "I"

    return numeral
