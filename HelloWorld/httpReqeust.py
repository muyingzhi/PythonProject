import urllib.request

url = 'http://www.baidu.com/s?wd=cloga'
html = urllib.request.urlopen(url).read()
print(html)