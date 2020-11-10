n = int(input("please insert an integer:"))


if n < 0:
  print("your given number is negative, so it can not be calculated.")

elif n == 0 or n == 1:
  print("your numbers factoriel is 1.") 

else:
  factoriel = 1
  for i in range(1,n+1):
    factoriel *= i
  print(factoriel)
  