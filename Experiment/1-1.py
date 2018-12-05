#coding=utf-8
# File    : 1-1.py
# Desc    :
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/10/17 19:06

def main():
	J = input("J = ")
	S = input("S = ")
	count = 0
	for s in S:
		if s in J:
			count += 1
	print(count)

if __name__=="__main__":
	main()