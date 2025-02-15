lst=[5,4,-4,-9,4,3,8,-10]
nested=[lst[i:i+3] for i in range(0,len(lst),3)]
print(nested)