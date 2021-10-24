def add_string(str1):

  length = len(str1)

  if length > 2:

    if str1[-3:] == 'polis':

      str1 += 'CS'

    else:

      str1 += 'polis'

  return str1



print(add_string('abc'))

print(add_string('Acropolis'))
