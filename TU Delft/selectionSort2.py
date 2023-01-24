import sys
    
def sort_B(l):
  for i in range(len(l)):
    mini = sys.maxsize
    for j in range(i, len(l)):
      if (l[j] < mini):
        mini = l[j]

    index = l.index(mini)
    temp = l[i]
    l[i] = l[index]
    l[index] = temp
  return l
    

print(sort_B([]))  # Add items to the list here, separated by commas
