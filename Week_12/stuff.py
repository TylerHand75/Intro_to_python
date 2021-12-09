Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input ("please enter your full name")
please enter your full name tyler irvin hand 
>>> names = name.slpit()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    names = name.slpit()
AttributeError: 'str' object has no attribute 'slpit'
>>> names = names.split()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    names = names.split()
NameError: name 'names' is not defined
>>> names = name.split()
>>> out = ''
>>> for n in names
SyntaxError: invalid syntax
>>> outfor n in names:
	
SyntaxError: invalid syntax
>>> for n in names:
	out += n[0] + '. '

	
>>> 
>>> out.strip()
't. i. h.'
>>> months = ['','january','febuary','march','april','may','june','july','auguest','september','october','novenber','december']
>>> date =  