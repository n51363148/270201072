def get_reversed_iterative(my_list):
  reversed_list = []
  for element in my_list:
    reversed_list = [element] + reversed_list
  return reversed_list

list1 = [1,2,3]
x = get_reversed_iterative(list1)
print(x)

################ Iterative reverse list finding



