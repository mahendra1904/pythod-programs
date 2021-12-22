Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> y=037
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> z=0o98
SyntaxError: invalid digit '9' in octal literal
>>> 
>>> 56thnumber=3300
SyntaxError: invalid syntax
>>> !Taylor='Instant'
SyntaxError: invalid syntax
>>> this variable=87.E02
SyntaxError: invalid syntax
>>> float=.17E-03
>>> print(float)
0.00017
>>> FLOAT=.17-03
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> FLOAT=.17E-03
>>> print(FLOAT)
0.00017
>>> temperature = 90
>>> print(temperature)
90
>>> a=30
>>> b=a+b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b=a+b
NameError: name 'b' is not defined
>>> a=10
>>> b=20
>>> print(a,b)
10 20
>>> print(a And b)
SyntaxError: invalid syntax
>>> print(a;b)
SyntaxError: invalid syntax
>>> a,b=10,20
>>> print(a)
10
>>> print(b)
20
>>> a,b=b,a
>>> print(a)
20
>>> 