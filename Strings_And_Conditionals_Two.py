def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False
  
print(contains("watermelon", "melon"))

def common_letters(string_one, string_two):
  modified_string_two = []
  subresult = []
  for letter in string_two:
    if letter in string_one:
      subresult.append(letter)
  result = set(subresult)
  return list(result)

print(common_letters('manhattan', 'san francisco'))