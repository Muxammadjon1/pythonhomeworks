tpl=(1,3,4,4,5,6,7,3,42,3,3,3)
unique_tpl=tuple(x for x in tpl if tpl.count(x)==1)
print(unique_tpl)