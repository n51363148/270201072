# I assumed that all exams have same percentage 
grades = [[70,90,100],[100,60,80],[100,100,95]]
average_notes = []
for grade in grades:
  mt1 = grade[0]
  mt2 = grade[1]
  fn =  grade[2]

  average = mt1  + mt2 + fn
  average /= 3
  if average > 90:
    average_notes.append(average)
    print(average_notes)
 