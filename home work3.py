#Q1
text = input("Enter a string :")
vowels = "aeiouAEIOU"
count =0
for char in text :
    if char in  vowels:
        count +=1
        print(f"Number of vowels :{count}")
#Q2
numbers = {10, 55, 2, 89, 43}
print(f"The Set is: {numbers}")
largest = None
for num in numbers:

    if largest is None or num > largest:
        largest = num

print(f"Largest number is: {largest}")
#Q3
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
#Q4
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"Original: {original_list}")
print(f"After removing duplicates: {unique_list}")
#Q5
num = int(input("Enter the number: "))

print(f"Multiplication Table for {num}:")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
#Q6
list1 = [1, 5, 3, 8]
list2 = [2, 5, 7, 8]
common = []
for x, y in zip(list1, list2):
    if x == y:
        common.append(x)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements at same index: {common}")
#Q7
pwd = input("Enter a password: ")
is_long = len(pwd) >= 8
has_upper = any(c.isupper() for c in pwd)
has_lower = any(c.islower() for c in pwd)
has_digit = any(c.isdigit() for c in pwd)
if is_long and has_upper and has_lower and has_digit:
    print("Password is Valid")
else:
    print("Password Invalid! It must have 8 chars, Upper, Lower, and a Digit.")
#Q8
def say_good_morning():
    print("Good Morning!")
say_good_morning()
#Q9

def greet_user(name):
    print(f"Hello, {name}!")
user_input = input("Enter your name: ")
greet_user(user_input)
#Q10

def print_sum(num1, num2):
    total = num1 + num2
    print(f"The sum is: {total}")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print_sum(n1, n2)
#Q11
def calculate_area(width, height):
    area = width * height
    return area
w = float(input("Enter width: "))
h = float(input("Enter height: "))
result = calculate_area(w, h)
print(f"The rectangle area is: {result}")
#Q12
def print_max_number(my_list):
    if len(my_list) == 0:
        print("The list is empty!")
        return

    largest = my_list[0]
    for num in my_list:
        if num > largest:
            largest = num

    print(f"The largest number in the list is: {largest}")

numbers = [15, 82, 7, 44, 91, 23]
print_max_number(numbers)
#Q13
def reverse_string(text):

    reversed_text = text[::-1]
    return reversed_text
user_str = input("Enter a string to reverse: ")
result = reverse_string(user_str)
print(f"Original: {user_str}")
print(f"Reversed: {result}")
#Q14
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result
num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is: {calculate_factorial(num)}")
#Q15
def check_login(username, password):
    correct_user = "admin"
    correct_pass = "1234"
    if username == correct_user and password == correct_pass:
        return True
    else:
        return False
user = input("Enter Username: ")
pwd = input("Enter Password: ")
if check_login(user, pwd):
    print("Login Successful! Welcome.")
else:
    print("Invalid Username or Password. Try again.")
#Q16

import random
def guess_game():
    target_number = random.randint(1, 100)

    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))

        if guess > target_number:
            print("Too high! Try again.")
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Correct! You guessed the number.")
            break
guess_game()

















