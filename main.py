# TASK: Write a program that checks if a word is a palindrome.

# Prompt the user to enter a string  
word=(input("enter the word to check if it's a palindrome ")).strip()

# Reverse the string by slicing 
word2 = word[::-1]

# Check if the original string is equal to the reversed string  
# If they are equal, it's a palindrome  
# If they are not equal, it's not a palindrome  

while True:
    if word2==word:
        print("this word is a palindrome")
        break
    else:
        print("this word is not a palindrome")
        break

