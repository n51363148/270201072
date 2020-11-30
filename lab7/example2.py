books = ["ULYESS","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]


book_dictionary = {}
for i in range(len(books)):
  key = books[i]
  charachters = len(key)
  unique_charachters = len(set(key))
  value = (charachters,unique_charachters)
  book_dictionary[key] = value
 
print(book_dictionary)


