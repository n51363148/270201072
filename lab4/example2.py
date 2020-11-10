x = int(input("please enter a year:"))

if x % 4 == 0:
  if  (x % 100 != 0) and (x % 4 == 0) :
    print(x,"is a leap year.")

  else:
    print(x,"is not a leap year.")



else:
  print(x,"is not a leap year.")