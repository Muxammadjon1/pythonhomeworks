num=[1,2,3,4,5,6,7,8,9]
sub_num=[1,2,9]
if all(item in num for item in sub_num):
    print("Sublist")
else: 
    print('It is not sublist')