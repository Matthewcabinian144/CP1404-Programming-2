score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")99

#version 1

"""With Strings and Functions"""

def main():
    score = float(input("Input Score number: "))
    print(score_status(score))


