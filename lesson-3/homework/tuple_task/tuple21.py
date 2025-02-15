tpl=(1,3,4,4,5,6,7,3,42,3,3,3)
 
new_tpl = tuple(x for x in tpl for _ in range(3))  
print(new_tpl)  