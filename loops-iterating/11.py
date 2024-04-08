my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_i = 0

while outer_i < len(my_list):
    inner_i = 0
    while inner_i < len(my_list[outer_i]):
        number = my_list[outer_i][inner_i]
        if number % 2 == 0:
            print(number)
        
        inner_i += 1
    outer_i += 1
