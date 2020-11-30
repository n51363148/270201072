
employees = {}

for _ in range(5):
  name = input("Enter name:")
  salary = int(input("Enter a salary:"))
  employees[name] = salary

print(employees)