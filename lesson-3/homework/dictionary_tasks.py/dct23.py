dct={
    'name':'John',
    'age':18,
    'surname':'Brown',
    'hobby':'Reading book',
    'hobby':'Football'
}
dct2={
    'name2':'John',
    'age1':18,
    'surname':'Brown',
    'hobby1':'Reading book',
    'hobby':'Football'
}
common_keys=set(dct.keys())&set(dct2.keys())
print(common_keys)

  