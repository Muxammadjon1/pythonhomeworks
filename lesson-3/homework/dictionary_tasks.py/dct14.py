dct={
    'name':'John',
    'age':18,
    'surname':'Brown',
    'hobby':'Reading book',
    'a':'Brown'
}
keys_with_value={key for key, value in dct.items() if value=='Brown'}
print(keys_with_value)