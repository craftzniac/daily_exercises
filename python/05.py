"""Task: Write a code to return `True` if the list's first and last numbers are the same. If the numbers are different, return `False`

Example:

Given:
numbers_x = [10, 20, 30, 40, 10]

Expected output:
Given list: [10, 20, 30, 40, 10]
result is True


Given:
numbers_y = [75, 65, 35, 75, 30]

Expected output:
Given list: [75, 65, 35, 75, 30]
result is False
"""

from typing import List
import unittest


def check_first_last_equal(nums: List[int]):
    if len(nums) == 0:
        return False
    first = nums[0]
    last = nums[-1]

    if first == last:
        return True
    else:
        return False


class TestFns(unittest.TestCase):
    def test_check_first_last_equal(self):
        self.assertTrue(check_first_last_equal([10, 20, 30, 40, 10]))

    def test_check_first_last_not_equal(self):
        self.assertFalse(check_first_last_equal([75, 65, 35, 75, 30]))


if __name__ == "__main__":
    nums = [23, 10, 29, 12, 23]
    result = check_first_last_equal(nums)
    print(f"Given list: {nums}\nresult is {result}")
    print("=====================")
    unittest.main()
