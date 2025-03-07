"""Task: Generate 3 random integers between 100 and 999 which is divisible by 5"""

import random


def int_between_100_999() -> int:
    num = random.randint(100, 999)
    return num if num % 5 == 0 else int_between_100_999()


def get_3_randoms():
    for _ in range(3):
        print(int_between_100_999())


if __name__ == "__main__":
    get_3_randoms()
