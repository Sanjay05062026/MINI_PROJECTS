import string
import secrets
import random

letters = string.ascii_letters  # lowercase + uppercase
numbers = string.digits
symbols = string.punctuation

# secrets is made for passwords; random is not secure enough
secure_random = random.SystemRandom()


def ask_number(prompt):
    """Keep asking until the user types a whole number that is 0 or more."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter 0 or a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input, please enter a number.")


num_letters = ask_number("Enter the number of letters you want : ")
num_numbers = ask_number("Enter the number of numbers you want : ")
num_symbols = ask_number("Enter the number of symbols you want : ")

if num_letters + num_numbers + num_symbols == 0:
    print("Password can't be empty. Run the program again.")
else:
    password_list = []
    for _ in range(num_letters):
        password_list.append(secrets.choice(letters))
    for _ in range(num_numbers):
        password_list.append(secrets.choice(numbers))
    for _ in range(num_symbols):
        password_list.append(secrets.choice(symbols))

    secure_random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is : {password}")
