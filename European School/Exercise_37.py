#input user
userInput = input("enter a letter: ")
#define vowel array
array = ["a", "e", "i", "o", "u"]
#if else statements
if userInput in array:
    print("your letter is a vowel")
elif userInput == "y":
    print("your letter is sometimes a consonant and sometimes a vowel")
else:
    print("your letter is a consonant")
