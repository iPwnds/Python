import sys


def sort_A(l):
  for i in range(len(l)):
    mini = sys.maxsize
    index = i
    for j in range(len(l)):
      if l[j] < mini:
        index = j
        mini = l[j]
    
    temp = l[i]
    l[i] = l[index]
    l[index] = temp
  return l


print(sort_A([]))  # Expand the list here with numbers separated by commas.