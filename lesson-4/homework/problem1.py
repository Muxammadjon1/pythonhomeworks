lst=[1,2,3]
lst2=[2,3,4]
uncommon=[x for x in lst if x not in lst2]+[x for x in lst2 if x not in lst]
print(uncommon)