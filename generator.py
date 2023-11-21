import random
import string
import pyperclip
import linecache

# Generate by random ASCII characters
def generate_password(length=32, include_numbers=True, include_special_chars=True):
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Generate by random words
def generate_password_2(num=6):
    output = ""
    for _ in range(num):
        output += get_word() + "-"
    return output[:-1]


def get_word():
    num_lines = sum(1 for _ in open('wordlist.txt', 'r'))
    line_number = random.randint(1, num_lines)
    line = linecache.getline('wordlist.txt', line_number)
    return line.strip("\n")


def true_or_false(s="y"):
    if s == "n":
        return False
    else:
        return True


def generate():
    mode = input("Do you want to generate a password with CHARACTERS or WORDS? (c/w): ").lower()
    # mode = "c"

    match mode:
        case "c":
            num = input("How many words do you want your password to have? (default: 6): ")
            # num = 6

            if num == "":
                num = 6
            else:
                num = int(num)

            pwd = generate_password_2(num)
        case _:
            has_numbers = true_or_false(input("Do you want to include NUMBERS in your password? (y/n): "))
            has_special_chars = true_or_false(input("Do you want to include SPECIAL CHARACTERS in your password? (y/n): "))
            length = input("How long do you want your password to be? (default: 32): ")
            if length == "":
                length = 32
            else:
                length = int(length)

            pwd = generate_password(length, has_numbers, has_special_chars)



    pyperclip.copy(pwd)
    print(f"Your password is: {pwd} (Already copied to the clipboard)")

