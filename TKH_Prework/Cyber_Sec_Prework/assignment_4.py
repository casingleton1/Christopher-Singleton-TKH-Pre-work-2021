>>> for name in names:
...     print(name)
... 
bob
jimmy
max b
jordan
future hendrix
>>> for name in names:
...     if len(name) > 14: print(name)
... 
>>> for name in names:
...     if len(name) < 14: print(name)
... 
bob
jimmy
max b
jordan
>>> for name in names:
...     if len(name) > 14: print(name)
...     else: print(longest_name)
... 
future hendrix
future hendrix
future hendrix
future hendrix
future hendrix
