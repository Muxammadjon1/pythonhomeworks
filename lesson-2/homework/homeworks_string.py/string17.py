user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
symbol = "*"
result = ""
for char in user_string:
    if char in vowels:
        result += symbol
    else:
        result += char
print("Result:", result)

