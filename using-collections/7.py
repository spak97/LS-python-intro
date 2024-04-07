info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)
print(parts)

info.replace(':', '+')

#8 line 3 is finding f from a new str text[21:35] 
# line 4 is finding f between indexes 21 and 35 from the original str