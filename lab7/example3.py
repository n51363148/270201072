
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dictionary = {}


for i in range(len(books)):
  key = books[i]
  character = len(key)
  unique_character = len(set(key))
  value = (character,unique_character)
  book_dictionary[key] = value

print(book_dictionary)




for book in books:
  character,unique_character = book_dictionary[book]
  avg = (character + unique_character) / 2
  book_dictionary[book] = (character,unique_character,avg)

print(book_dictionary)