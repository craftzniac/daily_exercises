"""Task: print the following pattern

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def solution1():
    for i in range(1, 6):
        sp = str(i) * i
        res = " ".join([*sp])
        print(res)


if __name__ == "__main__":
    solution1()
