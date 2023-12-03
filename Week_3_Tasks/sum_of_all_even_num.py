# Write a Python program to find and print the sum of all 
# the even numbers from 1 to 50 (inclusive). 
# Additionally, for each even number, if it is a multiple of 3,
# print "Three" instead of the number; if it is a multiple of 5, 
# print "Five" instead of the number. Finally, print the 
# total sum and the count of numbers replaced with "Three" or "Five."

total_sum = 0
count_three = 0
count_five = 0

for num in range(1, 51):
    if num % 2 == 0:
        total_sum += num
        if num % 3 == 0:
            print("Three")
            count_three += 1
        elif num % 5 == 0:
            print("Five")
            count_five += 1
        else:
            print(num)
            
print("\nTotal Sum:", total_sum)
print("Count of numbers replaced with 'Three':", count_three)
print("Count of numbers replaced with 'Five':", count_five)
