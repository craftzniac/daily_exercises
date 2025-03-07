"""Task: Get each digit from a number in the reverse order

For example,
If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
"""


def reverse_number(num: int):
    return " ".join([i for i in reversed(str(num))])


if __name__ == "__main__":
    result = reverse_number(7536)
    assert result == "6 3 5 7", "result was supposed to be '6 3 5 7'"
