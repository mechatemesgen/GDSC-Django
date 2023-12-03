# Write a program that prints the following pattern.
# The program should accept the input for character
# The pattern consists of a series of lines
# The characters in each line should follow a specific pattern based on the line number.
# Use conditional statements to determine the pattern for each line.
# Use a loop to iterate through the lines and print the characters accordingly.
# You are not allowed to use functions in your code.
# Do not store the pattern or any intermediate results in variables.

character = input("Enter a character: ")

for i in range(1, 6):
    for j in range(i):
        if i % 2 == 0:
            print(character, end="")
        else:
            print(character, end="")
    print()

