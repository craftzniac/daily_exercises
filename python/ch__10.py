"""Task:  Given two lists of numbers, write a Python code to create a new list such that the
latest list should contain odd numbers from the first list and even numbers from the second list.

Given:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

Expected output:
result list: [25, 35, 40, 60, 90]
"""

from typing import List


def merge_lists(list1: List[int], list2: List[int]):
    new_list = []
    for num in list1:
        if num % 2 == 1:  # check if num is odd
            new_list.append(num)

    for num in list2:
        if num % 2 == 0:  # check if num is even
            new_list.append(num)

    return new_list


if __name__ == "__main__":
    new_list = merge_lists([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])
    assert [
        25,
        35,
        40,
        60,
        90,
    ] == new_list, "new_list must be equal to [25, 35, 40, 60, 90]"
