def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    user_name = first_name + last_name
  else:
    user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = user_name[-1] + user_name[0:len(user_name) -1]
  return password

print(username_generator("Abe", "Simpson"))
username = username_generator("Abe", "Simpson")
print(password_generator(username))
  