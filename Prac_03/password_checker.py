MINIMUM_LENGTH = 4

def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisk(password)


def get_password(MINIMUM_LENGTH):
    password = input("Enter your password minimum of {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Invalid: Password Too Short")
        password = input("Enter your password minimum of {} characters: ".format(MINIMUM_LENGTH))
    return password


def print_asterisk(sequence):
    print('*' * len(sequence))

main()
