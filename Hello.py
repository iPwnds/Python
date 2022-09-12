First_Name = input("What is your First Name: \n")
Last_Name = input("What is your Second Name: \n")
Gender = input("What is your gender: \n")

if Gender == 'Male':
    print('Hello Mr, ' + First_Name + ' ' + Last_Name)

if Gender == 'Female':
    print('Hello Ms, ' + First_Name + ' ' + Last_Name)