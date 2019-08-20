import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    amount_of_quick_picks = int(input("How many quick picks? "))
    while amount_of_quick_picks < 0:
        print("Invalid, doesn't make sense")
        amount_of_quick_picks = int(input("How many quick picks? "))





main()
