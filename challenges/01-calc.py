# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What calculation would you like to do? (add, subtract, multiply, divide) ')


num1 = input('What is number 1? \n ')


num2 = input('What is number 2? ')


def result():
    if operator == 'add':
        return int(num1) + int(num2)
    elif operator == 'subtract':
        return int(num1) - int(num2)
    elif operator == 'multiply':
        return int(num1) * int(num2)
    elif operator == 'divide':
        return int(num1) / int(num2)

print(f"Your result is {result()}")
