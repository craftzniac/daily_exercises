"""Task: Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

Note: you must adhere to the following conditions:
- The lottery number must be 10 digits long.
- All 100 ticket number must be unique.

Hint: Generate a random list of 1000 numbers using randrange() and then use the sample() method to pick lucky 2 tickets.
"""

from random import sample, randrange


def gen_10_random():
    nums = []
    for _ in range(10):
        nums.append(randrange(1000000000, 9999999999))
    return nums


if __name__ == "__main__":
    random_10 = gen_10_random()
    two_lucky_winners = sample(random_10, 2)
    print(two_lucky_winners)
