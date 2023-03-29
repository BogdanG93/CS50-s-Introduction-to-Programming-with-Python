"""In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who
isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,”
and so he asks for $100. The bank’s manager proposes a compromise:
“You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.

Here’s how to test your code manually:

Type 'Hello' and press Enter. Your program should output:
$0
Type 'Hello, Newman' and press Enter. Your program should output:
$0
Type 'How you doing?' and press Enter. Your program should output
$20
Type 'What's happening?' and press Enter. Your program should output
$100"""

greetings = input('Greeting: ').lower().strip()
cash = 0
if greetings[0:5] == 'hello':
    cash = 0
elif greetings[0] == 'h':
    cash = 20
else:
    cash = 100
print('$' + str(cash))
