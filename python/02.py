"""Task: Write a python code to accept a string from the user and display characters present at an even index number

For example, str = "PYnative". So your code should display 'P', 'n', 't', 'v'

Expected output:
Orginal String is  PYnative
Printing only even index chars
P
n
t
v
"""


def get_user_string() -> str:
    while True:
        value = input("Enter a string: ")
        if len(value) != 0:
            return value
        else:
            print("Come on bro, that was empty space\n")


def print_even_index():
    text = get_user_string()
    print("Original String is PYnative")
    print("Printing only even index chars")
    for index, character in enumerate(text):
        if index % 2 == 0:
            print(character)


if __name__ == "__main__":
    print_even_index()
