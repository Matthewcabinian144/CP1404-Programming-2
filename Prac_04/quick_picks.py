import random

numbers_per_line = 6
maximum = 45
minimum = 1

def main():
    amount_of_quick_picks = int(input("How many quick picks? "))
    while amount_of_quick_picks < 0:
        print("Invalid, doesn't make sense")
        amount_of_quick_picks = int(input("How many quick picks? "))

    for i in range(amount_of_quick_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))
main()
