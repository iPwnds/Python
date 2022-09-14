#Question: Write a program that asks the user to enter his or her name. The program should respond with a message that says hello to the user, using his or her name.
#Criteria: Exercise 2: Hello (9 Lines)

First_Name = input("What is your First Name: \n")
Last_Name = input("What is your Second Name: \n")
Gender = input("What is your gender: \n")

if Gender == 'Male':
    print('Hello Mr, ' + First_Name + ' ' + Last_Name)

if Gender == 'Female':
    print('Hello Ms, ' + First_Name + ' ' + Last_Name)