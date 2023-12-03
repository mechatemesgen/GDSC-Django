def add():
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    sum = int (num1 + num2)
    print(f"The sum of {num1} and {num2} is: {sum}")
add()

def sub():
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    deff = int (num1 - num2)
    print(f"The deffirence b/n {num1} and {num2} is: {deff}")
sub()

def mul():
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    prod = int (num1 * num2)
    print(f"The Product of {num1} and {num2} is: {prod}")
mul()

def div():
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    sum = int (num1 / num2)
    print(f"If {num1} is divided by {num2} the answer is: {div}")
div()

print("Enter [1] for addition.")
print("Enter [2] for subtraction.")
print("Enter [3] for Multiplication.")
print("Enter [4] for division.")
print("Enter [0] to Exit the program.")
choose = int(input("Enter Your Choose: "))

if choose == 1:
    add()
elif choose ==2:
    sub()
elif choose == 3:
    mul()
elif choose == 4:
    div()
