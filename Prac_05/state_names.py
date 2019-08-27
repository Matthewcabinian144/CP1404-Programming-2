"""
CP1404 Practical 5
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for state in STATE_NAMES:
    print("{} is in {}".format(state, STATE_NAMES[state]))

state = str(input("Enter short state: "))
while state.upper() != "":
    if state.upper() in STATE_NAMES:
        print(state, "is", STATE_NAMES[state.upper()])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
