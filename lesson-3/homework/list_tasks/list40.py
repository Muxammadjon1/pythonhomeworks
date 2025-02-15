lst=[1,2,3,2,1,2,3,5,433,23,344,233,433,344]
new_lst=[i for i in lst if lst.count(i)==1 ]
print(new_lst)