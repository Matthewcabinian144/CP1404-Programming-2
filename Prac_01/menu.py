"""CP1404 Practice & Extension Work: Menu"""

username = str(input("Enter your username: "))
print("(H)ello\n(G)oodbye\n(Q)uit\n")
choice = input("\n>>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello",username)
    elif choice == "G":
        print("Goodbye",username)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    choice = input("\n>>>").upper()
print("Finished.")
