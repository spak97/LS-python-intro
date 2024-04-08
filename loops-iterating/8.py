my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

names = { f'{name}': len(name) 
         for name in my_set 
         if len(name) % 2 != 0}

print(names)

