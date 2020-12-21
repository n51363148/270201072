def iterative_evens(list_integers):
  count = 0
  for number in list_integers:
    if number % 2 == 0:
      count += 1
  return count


list1 = [1,2,3]
x = iterative_evens(list1)
print(x)

################## Iterative type for findind the number of even numbers

def get_even_numbers(my_list):
  if len(my_list) == 0:
    return 0
  else:
    if my_list[0] % 2 == 0:
      return 1 + get_even_numbers(my_list[1:])
    else:
      return 0 + get_even_numbers(my_list[1:])

my_list = [2,3,5,7]
x = get_even_numbers(my_list)
print(x)


################## Recursive type for finding the even numbers