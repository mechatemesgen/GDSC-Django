# Develop a program that checks if a user-inputted word is 
# a palindrome. A palindrome is a 
# word that reads the same backward as forward (e.g., "radar").

word = input("Enter a word: ")

cleaned_word = ''.join(word.split()).lower()

if cleaned_word == cleaned_word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
