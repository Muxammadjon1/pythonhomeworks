from collections import defaultdict

my_dict = defaultdict(lambda: "Default Value")
my_dict["a"] = 1
my_dict["b"] = 2

print(my_dict["a"]) 
print(my_dict["c"])  