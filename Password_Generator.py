import string
import random

letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

num_letters = int(input("Enter the number of letters you want : "))
num_numbers = int(input("Enter the number of numbers you want : "))
num_symbols = int(input("Enter the number of symbols you want : "))

password_list = []

for i in range(1, num_letters+1):
    password_list.append(random.choice(letters))
for i in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))
for i in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))
print(password_list)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")