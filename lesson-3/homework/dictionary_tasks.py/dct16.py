my_dict = {
    "name": "Alice",
    "age": 25,
    "address": {"city": "New York", "zip": "10001"},
    "contact": "123-456-7890"
}
has_nested_dict = any(isinstance(value, dict) for value in my_dict.values())
print(has_nested_dict)  