>>> for names in names_list:
...     print(names)
... 
bob
jimmy
max b
bernie
jordan
future hendrix
>>> for names in names_list:
...     if len(names)%2==0: print(names)
... 
bernie
jordan
future hendrix
>>> for names in names_list:
...     if len(names)%2==1: print(names)
... 
bob
jimmy
max b
>>> names_list[4] = "bordan"
>>> names_list[5] = "buture hendrix"
>>> print(names_list)
['bob', 'jimmy', 'max b', 'bernie', 'bordan', 'buture hendrix']
>>> names_list[0] = "boc"
>>> names_list[1] = "jimmc"
>>> names_list[2] = "max c"
>>> print(names_list)
['boc', 'jimmc', 'max c', 'bernie', 'bordan', 'buture hendrix']
>>> for names in names_list:
...     if len(names)%2==0: print(names)
... 
bernie
bordan
buture hendrix
>>> for names in names_list:
...     if len(names)%2==1: print(names)
... 
boc
jimmc
max c
>>> def even_list():
...     return "['bernie', 'bordan', 'buture hendrix']"
... 
>>> print (even_list)
['bernie', 'bordan', 'buture hendrix']
>>> 