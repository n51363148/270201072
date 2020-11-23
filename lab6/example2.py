grades = [[50,90,60],[15,60,75],[99,95,91]]


average_grades = []

for grade in grades:
  mt1 = grade[0]
  mt2 = grade[1]
  final = grade[2]

  average = mt1 * 0.3 + mt2 * 0.3 + final * 0.4

  average_grades.append(average)

  print(average_grades)