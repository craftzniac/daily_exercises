"""Task: Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse.

For example, 545 is a palindrome number.

Given: 121
Expected output:
Yes, 121 is palindrome

Given: 125
Expected output:
No, 125 is not palindrome

"""


def check_palindrome(num: int):
    # convert number to a string
    num_string = str(num)

    # divide by 11 if the number has even number of digits
    if len(num_string) % 2 == 0:
        # every palindrome with an even number of digits is divisible by 11
        if num % 11 == 0:
            return True

    ## For numbers with an odd number of digits
    # split into a list of digits
    digits = list(num_string)

    # loop on the digits for num_of_digits/2  i.e from the beginning to the middle of the list
    iter_count = len(digits) // 2  # don't care about the middle value
    front_index = 0
    back_index = -1
    while front_index < iter_count:
        # read from both the front and back of the list
        print(f"front: {front_index}, back: {back_index}")
        if digits[front_index] != digits[back_index]:
            return False
        front_index += 1
        back_index -= 1
    else:
        return True


if __name__ == "__main__":
    num = 121121
    if check_palindrome(num) == True:
        print(f"Yes, {num} is palindrome")
    else:
        print(f"No, {num} is NOT palindrome")
