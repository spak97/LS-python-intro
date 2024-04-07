pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets["Dog"])

print(pets.get('Lizard'))

print(pets.get("Lizard", "<silence>"))

#5 lists, sets, and dicts because they are mutable

#6
print('abc-def'.isalpha()) 
print('abc_def'.isalpha())
print('abc def'.isalpha())
print('abc def'.isalpha() and
      'abc def'.isspace())
print('abc def'.isalpha() or
      'abc def'.isspace())
print('abcdef'.isalpha())
print('31415'.isdigit())
print('-31415'.isdigit())
print('31_415'.isdigit())
print('3.1415'.isdigit())
print(''.isspace())