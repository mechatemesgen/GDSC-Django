#Write a Python program that takes a sentence as input and generates a list containing the 
#lengths of each word in the sentence. Use list comprehension for this task.
string = input("Enter String: ")
word_len= [len(str) for str in string.split()]
print(word_len)
 
