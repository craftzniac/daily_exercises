"""Task: Write a Python code to display numbers from a list divisible by 5

Example:
Given: list is  [10, 20, 33, 46, 55]

Expected output:
Divisible by 5
10
20
55
"""

from typing import List
import unittest


def div_by_5(nums: List[int]) -> List[int]:
    div_by_5 = []
    for num in nums:
        if num % 5 == 0:
            div_by_5.append(num)
    return div_by_5


class TestFns(unittest.TestCase):
    def test_div_by_5(self):
        self.assertEqual([10, 20, 55], div_by_5([10, 20, 33, 46, 55]))


if __name__ == "__main__":
    print("Divisible by 5\n")
    # unittest.main()
    result = div_by_5([10, 20, 33, 46, 55])
    for num in result:
        print(num)
