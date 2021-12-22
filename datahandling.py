Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bool(0)
False
>>> bool(str(0))
True
>>> 6==input(5+4/2)
7.0
False
>>> 6==int(input(5+4/2))
7.0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    6==int(input(5+4/2))
ValueError: invalid literal for int() with base 10: ''
a
>>> a,b,c=2,3,6
>>> d=a+b*c/b
>>> print(d)
8.0
>>> a=va=3
>>> b=va=3
>>> print(a,b)
3 3
>>> a=3
>>> b=3.0
>>> print(a==b)
True
>>> print(a is b)
False
>>> a,b,c=1,1,2
>>> d=a+b
>>> e=1.0
>>> f=1.0
>>> g=2.0
>>> h=e+f
>>> print(c==d)
True
>>> print(c is d)
True
>>> g==h
True
>>> g is h
False
>>> 