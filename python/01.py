"""Task: Given two integer numbers, write a python code to return their product only if the product is equal or lower than 1,000. Otherwise, return their sum

Example 1:
Given:
number1 = 20
number2 = 30

Expected Output:
The result is 600


Example 2;
Given:
number1 = 40
number2 = 30

Expected Output:
The result is 70
"""


def get_num(*, name: str) -> int:
    num = None
    """Get a number from user"""
    while num == None:
        try:
            num = int(input(f"Enter {name}: "))
            break
        except ValueError as err:
            print("Invalid input. Try again")
    return num


def mult_or_sum_of_nums(num1: int, num2: int) -> int:
    limit = 1_000
    product = num1 * num2
    if product <= limit:
        return product
    else:
        return num1 + num2


def main():
    num1 = get_num(name="number1")
    num2 = get_num(name="number2")
    result = mult_or_sum_of_nums(num1, num2)
    print(f"result: {result}")
    pass


if __name__ == "__main__":
    main()
