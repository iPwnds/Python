motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #this change the value of the first item in the list
print(motorcycles)

motorcycles.append('ducati') #you can add elements to the end of a list with the append method
print(motorcycles)

motorcycles = [] #you can create a empty list, to make the users fill it in

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati') #this inserts a certain item in a certain place of the list
print(motorcycles)

del motorcycles[0] #this deletes a specific item from the list, you can no longer acces the item once you del it (if you know the position) (statement)
print(motorcycles)
del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop() #you create a new list and pop the last item from the motorcycles list (last value, you can still access it) (method)
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['yamaha', 'honda', 'suzuki', 'ducati']

first_owned = motorcycles.pop(0) #you can also pop with an index which will pop the index that you put in
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('suzuki') #this removes the suzuki from the list (only once)
print(motorcycles)

too_expensive = 'ducati' #this will set the value 'ducati' to the variable 'too expensive'
motorcycles.remove(too_expensive) #use the var to tell python what value to get out of the list
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')