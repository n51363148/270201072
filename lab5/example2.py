n = int(input("How many numbers?:"))

for i in range(1,n+1):
  x = int(input("give an integer:"))
  if x%2 == 0:
    print(x/100)
  else:
    print("all of the numbers that you gave is odd")