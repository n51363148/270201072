x = int(input("how many numbers do you want to enter:"))
list1 = []
i = 1
while i <= x:
  i += 1
  n = int(input("please enter an integer:"))
  list1.append(n)
  unique_numbers = list(set(list1))
  unique_numbers.sort(reverse = True)
print(unique_numbers)  


