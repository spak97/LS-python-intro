obj = 'ABcd'
obj.upper()
obj = obj.lower()
print(len(obj))
obj = list(obj)
obj.pop()
obj[2] = 'X'
obj.sort()
set(obj)
obj = tuple(obj)

"""
reassign
neither
reassign 
neither
reassign
mutate
mutate
mutate
neither
reassign
"""