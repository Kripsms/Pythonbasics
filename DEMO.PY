'''1. What is Programming?

Programming is like giving step-by-step instructions to a computer.

Just like you give steps to cook noodles → “Boil water → Add noodles → Add masala → Serve”.

In coding, we give steps using a programming language like Python.

2. Basic Concepts They Need
🔹 Variables (Data Storage)

Think of variables as boxes where you store information.

Example:

name = "Alice"
age = 20


Here, name box has "Alice", and age box has 20.

🔹 Input and Output (Talking to the User)

Input = Asking the user to type something.

Output = Showing a result on the screen.

Example:'''


# name = input("Enter your name: ")
# print("Hello", name)


'''🔹 If/Else (Decision Making)

Computers make decisions using if/else.

Example:'''

# age = int(input("Enter your age: "))
# if age > 18:
#     print("You are an adult.")
# elif age == 18:
#     print("You just became an adult!")
# else:
#     print("You are a minor.")

'''🔹 Loops (Repetition)

A loop repeats instructions until we stop it.

Example:'''

# for i in range(15):
#     if i % 2 == 0:
#         print(i)
    



'''While loop keeps running until a condition becomes false.'''

# count = 1
# while count <= 3:
#     print("Hello")
#     count += 1


'''🔹 Lists (Collection of Data)

A list stores many values in one place.

Example:'''

# friends = ["Alice", "Bob", "Charlie"]
# print(friends[2]) 

numbers = [1, 2, 3, 4, 5]
print(numbers[2])


''''🔹 Functions (Reusable Actions)

Functions are like mini-machines that do a task when called.

Example:'''

def greet():
    print("Hello!")

greet() 

'''3. How Programs Run

You write instructions in a file → program.py

Run it → computer follows steps line by line.

If something is wrong → computer shows an error (which is normal, we fix it).

4. Demo Program to Show Them
# General Demo Program

# Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# If/Else
if age >= 18:
    print("Hello", name, "- You are an adult.")
else:
    print("Hello", name, "- You are a minor.")

# List
hobbies = ["reading", "coding", "gaming"]
print("Some hobbies:", hobbies)

# Function
def greet():
    print("Welcome to coding,", name)

greet()'''