lst=[1,2,3,4,5,6,1,2,34,234,12,4,3,23,323,123,234,1,9]
odd_count=sum(1 for num in lst if num%2==1)
print(odd_count)