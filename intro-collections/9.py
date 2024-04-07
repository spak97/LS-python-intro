my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 1 yes
# 2 no
# 3 yes
# 4 yes, for nested lists, list constructor doesn't 
# create a new object. Instead, it creates a shallow copy
# which is just a reference to the nested list

# 10
# not necessariy because its a set and sets aren't ordered