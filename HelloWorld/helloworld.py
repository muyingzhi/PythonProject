import os
import math
import urllib.request

print ("Hello World")

xrange = (1,10)
for x in xrange:
	print(x)
y = 1
#x = y if 1>0 else:8
print(x)

print("Content-type:text/html\r\n\r\n")
print("Environment")
for param in os.environ.keys():
	print ("<b>%20s</b>:%s</br>" ,param,os.environ[param])
add = lambda x,y: x*2 +y
print("x*2+y=",add(10,14))
print(1)

class Fish(object):
	"""docstring for Fish"""
	def eat(self, food):
		if food is not None:
			self.hungry = False
class User:
	def __init__(myself,name):
		myself.name = name

f = Fish()
Fish.eat(f,"earthworm")
f.eat("earthworm")
print("is hungry?",f.hungry)
u = User('Mikeson')
print(u.name)	
print(math.sin(math.pi/2))	
a = 10
b = 8
c = 9
print( a % b)
print( a // b)
print(a>b<c)

url = 'http://www.baidu.com/s?wd=cloga'
html = urllib.request.urlopen(url).read()
print(html)
