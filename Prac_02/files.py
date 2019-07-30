"""Do from Scratch Exercise: Files"""

#Exercise 1:
file_name_out =  open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=file_name_out)
file_name_out.close()

#Excercise 2:
file_name_in = open("name.txt", 'r')
name = file_name_in.read().strip()
file_name_in.close()
print("Your name is", name)

#Excercise 3:
file_numbers = open("numbers.txt", 'r')
number1 = int(file_numbers.readline())
number2 = int(file_numbers.readline())
print(number1 + number2)
file_numbers.close()

#Excercise 4:
