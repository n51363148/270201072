people =[("Jon",15),("Ned",45),("Arya",9),("Catelyn",44),("Bran",10)]

for person in people:
  if person[1] > 18:
    print(person[0])

for  person in people:
  name = person[0]
  age =  person[1]
  if age > 18:
    print(name)

for (x,y) in people:
  if y > 18:
    print(x)