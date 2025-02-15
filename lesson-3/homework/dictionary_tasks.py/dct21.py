my_dict = {"b": 2, "a": 1, "d": 4, "c": 3}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)  