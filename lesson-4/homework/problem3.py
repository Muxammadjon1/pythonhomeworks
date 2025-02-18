txt = input("Enter the string:")
vowels = "aeiou"
result = []
count = 0  

i = 0
while i < len(txt):
    result.append(txt[i])
    count += 1

    if count == 3:  
        if i + 1 < len(txt) and (txt[i] in vowels or (result and result[-1] == '_')):
            result.append(txt[i + 1])
            result.append('_')
            i += 1  
        else:
            result.append('_')
        count = 0  

    i += 1

output = "".join(result)
print(output) 