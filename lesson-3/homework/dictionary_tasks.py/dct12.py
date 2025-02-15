dct={
    'name':'John',
    'age':18,
    'surname':'Brown',
    'hobby':'Reading book',
    'Yaxshi':'Brown'
}
value_s=dct.values()
number_of_values=sum(1 for x in value_s if x=='J')
print(number_of_values)