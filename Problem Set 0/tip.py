"""In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically
an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
"""
# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")
#
#
# def dollars_to_float(d):
#     #
#
#
# def percent_to_float(p):
#     #
#
#
# main()
"""Well, we’ve written most of a tip calculator for you. Unfortunately, we didn't have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.

Here’s how to test your code manually:

Type $50.00 and press Enter. Then, type 15% and press Enter. Your program should output:
Leave $7.50    
Type $100.00 and press Enter. Then, type 18% and press Enter. Your program should output:
Leave $18.00
Type $15.00 and press Enter. Then, type 25% and press Enter. Your program should output
Leave $3.75"""


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar):
    dollar = float(dollar.replace('$', ''))
    return dollar


def percent_to_float(perc):
    perc = float(perc.replace('%', '')) / 100
    return perc


main()
