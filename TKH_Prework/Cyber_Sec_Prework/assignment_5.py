>>> print(names)
['bob', 'jimmy', 'max b', 'jordan', 'future hendrix']
>>> max(names)
'max b'
>>> longest(names)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'longest' is not defined
>>> max([names])
['bob', 'jimmy', 'max b', 'jordan', 'future hendrix']
>>> max(names)
'max b'
>>> len(names)
5
>>> greet(names)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in greet
TypeError: can only concatenate str (not "list") to str
>>> max(names, key = len)
'future hendrix'
>>> big_name = "future_hendrix"
>>> print(big_name)
future_hendrix
