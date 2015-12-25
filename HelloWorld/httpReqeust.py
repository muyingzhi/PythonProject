import urllib.request

url = 'http://www.baidu.com/s?wd=cloga'
resp = urllib.request.urlopen(url)
html = resp.read()
print(html)
print(resp.geturl())
print(resp.info())
try:
	res = 2 / 0
except:
	import sys
	tuple = sys.exc_info()
	for i in tuple:
		print(i)
with open("helloworld.py") as f:
	for line in f:
		print(line)
		
