authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)
subresult = []
author_last_names = []

for author in author_names:
  subresult.append(author.split(' '))

for author in subresult:
  author_last_names.append(author[1])

print(author_last_names)
