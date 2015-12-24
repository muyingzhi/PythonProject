import os
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