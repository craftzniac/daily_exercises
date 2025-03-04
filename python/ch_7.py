"""Task: Write a Python code to find how often the substring “Emma” appears in the given string.

Given:
str_x = "Emma is good developer. Emma is a writer"


Expected output:
Emma appeared 2 times
"""


def num_of_occurance(sub_string: str, text: str) -> int:
    # loop through each text
    count = 0
    i = 0
    while i < len(text):
        if text[i] == sub_string[0]:
            ## slice off the next chars of the text to see if they match sub_string
            peek = text[i : len(sub_string) + i]
            if sub_string == peek:
                count += 1
                # jump the cursor by the length of the sub_string so that you don't have to needlessly loop over those characters
                i += len(sub_string)
                continue  # avoid the i += 1 statement below
        i += 1
    return count


if __name__ == "__main__":
    count = num_of_occurance(
        "Emma",
        "Emma is a good developer. Emma is a writer. emma is here",  # "emma" does not count
    )
    print(f"Emma appeared {count} times")
