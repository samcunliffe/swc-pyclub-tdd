def to_roman(arabic: int) -> str:
    if arabic not in range(1, 4000):
        raise ValueError("Roman numerals only map to [1, 3999].")

    numeral = ""
    while arabic >= 10:
        arabic -= 10
        numeral += "X"

    while arabic >= 9:
        arabic -= 9
        numeral += "IX"

    while arabic >= 5:
        arabic -= 5
        numeral += "V"

    while arabic >= 4:
        arabic -= 4
        numeral += "IV"

    while arabic >= 1:
        arabic -= 1
        numeral += "I"
    return numeral
