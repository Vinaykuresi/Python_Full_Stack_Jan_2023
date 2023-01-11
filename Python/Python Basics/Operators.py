Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num_1 = 10
>>> num_2 = 20

>>> num_3 = num_1 + num_2
>>> num_3
30
>>> num_3 / 5
6.0
>>> num_3 = num_3 % 3
>>> num_3
0
>>> 
>>> num_1 > num_2
False
>>> num_3 <= num_1
True
>>> num_3 != num_1
True
>>> num_3 == 0
True
>>> num_3 != num_1
True
>>> 
>>> 
>>> (num_1 > num_2) and (num_2 < 30)
False
>>> 
>>> (num_1 > num_2) or (num_2 < 30)
True
>>> !((num_1 > num_2) and (num_2 < 30))
SyntaxError: invalid syntax
>>> not((num_1 > num_2) and (num_2 < 30))
True
