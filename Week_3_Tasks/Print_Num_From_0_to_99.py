# Write a program that prints numbers from 0 to 99.
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module


for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
