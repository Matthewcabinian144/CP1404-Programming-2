MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit : "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you for using Temperature Converter.")

#version 1

"""Version 2 with strings and fucntions"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = fahrenheit_calculation(celsius)
        print("Result: {:.2f} F".format(fahrenheit))

    elif choice == "F":
        fahrenheit = float(input("Fahrenheit : "))
        celsius = celsius_calculation(fahrenheit)
        print("Result: {:.2f} C".format(celsius))

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you for using Temperature Converter.")

def celsius_calculation(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def fahrenheit_calculation(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
