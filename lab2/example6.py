a = int(input("Please insert integer for a:"))
b = int(input("Please insert integer for b:"))
c = int(input("Please insert integer for c:"))

discriminant = (b**2) - (4*a*c)

d = int(discriminant)**0.5


if discriminant > 0:
  x1 = (-b+d)/2*a
  x2 = (-b-d)/2*a

  print(x1,x2, "are your roots.")

elif discriminant == 0:
  x3 = -b/2*a
  print(x3, "is your only one root")

else:
  print("There are two complex roots.")  