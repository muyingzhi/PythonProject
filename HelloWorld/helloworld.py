# -*- coding: UTF-8 -*-
import os,sys
import math
import urllib.request
import stocklib

# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

code = 'sz000503'
stock = stocklib.readStock(code)
print(str(stock))



# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
def dec2bin(num_string):
	num = int(num_string)
	mid = []
	while True:
		if num == 0 :break
		num,rem = divmod(num,2)
		mid.append(base[rem])
	print(mid)
	return ''.join([ str(x) for x in mid[::-1]])
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

meNum = str(ord("一"))
print(meNum)
print(dec2bin(meNum))
print(dec2hex(meNum))
print(chr(25105))

hnum = [123,78]
lnum = [89,90]
for h in range(0,256) :

	for m in range(0,16):
		row = ""
		for n in range(0,16):
			hex_h = dec2hex(str(h))
			hex_l = dec2hex(str(m*16+n))
			if m==0 :
				hex_l = "0"+hex_l
				#if n==0 : hex_l =  "00"
			#print(hex_l)
			row = row + "," + chr(int(hex_h+hex_l,16))
		print(dec2hex(str(h))+dec2hex(str(m*16+0))+":"+row)