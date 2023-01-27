def letter_check(word, letter):
  checker = False
  for litera in word:
    if litera == letter:
      checker = True
      break
    else:
      checker = False
  return checker

print(letter_check("strawberry", "a"))