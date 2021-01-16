import json

with open('text.txt', 'r') as my_file:
  my_dict = {}

  lines = my_file.readlines() 

  for line in lines:
    splittedLine = line.strip().split()
    my_dict[line[0:2]] = line[3:-1]

  with open('countries.js', 'w') as out_file:
    out_file.write('var countries = %s;' % json.dumps(my_dict))