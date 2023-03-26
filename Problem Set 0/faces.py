"""Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :(
was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns
that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any
:( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert
on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly,
as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

Here’s how to test your code manually:

Type Hello :) and press Enter. Your program should output:
Hello 🙂

Type Goodbye :( and press Enter. Your program should output:
Goodbye 🙁

Type Hello :) Goodbye :( and press Enter. Your program should output
Hello 🙂 Goodbye 🙁"""
def convert(user_input):
    user_input = user_input.replace(':)', '🙂').replace(':(', '🙁')
    return user_input

def main():
    input_from_keyboard = input('')
    input_from_keyboard = convert(input_from_keyboard)
    print(input_from_keyboard)

main()
