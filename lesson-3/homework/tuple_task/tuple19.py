tpl=(1,3,4,4,5,6,7,3,42,3,3,3)
lst_tpl=list(tpl)
if 3 in lst_tpl:
    lst_tpl.remove(3)
new_tuple=tuple(lst_tpl)
print(new_tuple)