lst=[1,2,3,4,5,6,1,2,34,234,12,4,3,23,323,123,234,1,9,20]

if len(lst)%2==1:
    print(lst[len(lst)//2+1])
else:
    print(lst[len(lst)//2-1],lst[len(lst)//2])