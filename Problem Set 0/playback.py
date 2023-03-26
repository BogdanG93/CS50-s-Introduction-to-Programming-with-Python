"""Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down,
a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and
then outputs that same input, replacing each space with ... (i.e., three periods).

Here’s how to test your code manually:

Type This is CS50 and press Enter. Your program should output:
This...is...CS50

Type This is our week on functions and press Enter. Your program should output:
This...is...our...week...on...functions

Type Let's implement a function called hello and press Enter. Your program should output
Let's...implement...a...function...called...hello"""
slow_down = input('').replace(' ', '...')
print(slow_down)
