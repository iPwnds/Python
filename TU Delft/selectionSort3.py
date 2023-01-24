import sys
    
def sort_C(l):
  for i in range(len(l)):
    mini = sys.maxsize
    index = i
    for j in range(i, len(l)):
      if (l[j] < mini):
        index = j
        mini = l[j]
    
    temp = l[i]
    l[i] = l[index]
    l[index] = temp
  return l


print(sort_C([]))   # Add items to the list here, separated by commas.