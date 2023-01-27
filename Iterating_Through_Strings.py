def get_length(string):
  counter = 0
  for letter in string:
    counter += 1
  return counter

print(get_length("hola"))