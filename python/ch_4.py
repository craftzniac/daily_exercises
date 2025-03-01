"""Task: Create a python code to remove characters from a string from 0 to n and return a new string

Example:
Give: `remove_chars("PYnative", 4)`
expected output: tive

Give: `remove_chars("PYnative", 2)`
expected output: native

n must be less than the lenght of the string
"""

import unittest


def remove_chars(text: str, n: int):
    if n > len(text):
        raise Exception("n must be less than length of the string")
    return text[n:]


class TestFns(unittest.TestCase):
    def test_remove_chars(self):
        self.assertEqual("tive", remove_chars("PYnative", 4))
        self.assertEqual("native", remove_chars("PYnative", 2))


if __name__ == "__main__":
    unittest.main()
