# Question 1:
# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

dictionary = {
    "namaste": "Hello",
    "shukriya": "Thank you",  
    "kripya": "Please",
    "pyaar": "Love",
    "dosti": "Friendship"
    
}
word = input("Enter a Hindi word to look up its English translation: ")
print(dictionary[word])
              