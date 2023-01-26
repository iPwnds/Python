numbers = [42, 23, 15, 1, 8, 16, 4]

print(numbers)

for i in range(0,len(numbers)):
    minimum = min(numbers[i:])
    min_index = numbers.index(minimum)
    
    numbers[min_index] = numbers[i]
    numbers[i] = minimum
    
    print(numbers)