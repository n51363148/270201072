x = int(input("please give a number:"))
list1 = []
list2 = []
i = 0
while i<= x-1:
  rows = 10**i
  i += 1
  list1.append(rows)
  list1.sort(reverse = True)



for m in list1:
  m = str(m)
  list2.append(m)


for n in range(0,x):
  identity = "0"*n + list2[n]
  print(identity)

  

  
