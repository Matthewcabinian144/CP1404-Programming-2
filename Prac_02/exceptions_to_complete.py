"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
results = 0
while not finished:
    try:
        """Code for input"""
        results = int(input("Enter a valid Integer: "))
        finished = True
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", results)
