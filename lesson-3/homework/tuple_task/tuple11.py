my_tuple = (1, 2, 3, 2, 4, 2, 5)
element_to_find = 2
indices = [index for index, value in enumerate(my_tuple) if value == element_to_find]
print("Indices:", indices)