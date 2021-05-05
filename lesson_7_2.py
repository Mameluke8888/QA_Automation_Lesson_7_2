# Exercise #1
# Create a program that will output everything in lowercase whatever the user will input. The program should run until the client enters the word “STOP”.
#
# Exercise #2
# You have a dictionary {'Jake': '$100K', 'Anand': '$120K'}. Using the string formatting print what salaries every person has.
#
# Exercise #3
# Given a 5 element tuple: (4, 30, 2017, 2, 27). Using the string formating print: '2 27 2017 4 30'
# Hint! use index numbers to specify positions.

# Exercise #1
typed_string = ""
while typed_string != "stop":
    typed_string = input("Please type a string: ")
    typed_string = typed_string.lower()
    print("Processed string (lower case): " + typed_string)
print("Thank you!")
print()

# Exercise #2
test_dict = {'Jake': '$100K', 'Anand': '$120K'}
for item in test_dict.items():
    print("Employee {0} salary is: {1}".format(item[0], item[1]))

# Exercise #3
test_tuple = (4, 30, 2017, 2, 27)
# print("{0} {1} {2} {3} {4}".format(1, 2, 3, 4, 5))
print("\n{0} {1} {2} {3} {4}".format(test_tuple[3], test_tuple[4], test_tuple[2], test_tuple[0], test_tuple[1]))
