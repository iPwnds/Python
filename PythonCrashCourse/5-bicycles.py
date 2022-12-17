bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #make a list that you can access like shown below
print(bicycles)

print(bicycles[0].title()) #use the index surrounded by square brackets to just print the element(s) from the list that you want

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #use the index number -1 to access the last element in a list and -2 for the second last and so forth

message = f"My first bicycle was a {bicycles[0].title()}." #you can use the values in the list just like a variable
print(message())