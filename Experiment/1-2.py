#coding=utf-8
# File    : 1-2.py
# Desc    :
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/10/17 19:14

def dfs(n, k, start, comb, ans):
	if not k:   #当k=0时，将当前组合添加到ans中
		ans.append(comb)
		return
	for i in range(start, n + 1):     # 1-4
		dfs(n, k - 1, i + 1, comb + [i], ans)

	# i = 1: self.dfs(4, 1, 2, [1], [])
		# i = 2: self.dfs(4, 0, 3, [1, 2], [])
		# i = 3: self.dfs(4, 0, 4, [1, 3], [])
		# i = 4: self.dfs(4, 0, 5, [1, 4], [])

	# i = 2: self.dfs(4, 1, 3, [2], [])
		# i = 3: self.dfs(4, 0, 4, [2, 3], [])
		# i = 4: self.dfs(4, 0, 5, [2, 4], [])

	# i = 3: self.dfs(4, 1, 4, [2], [])
		# i = 4: self.dfs(4, 0, 5, [3, 4], [])

	# i = 4: self.dfs(4, 1, 5, [2], [])
		# range(5, 5) 终止

	# n: 数字范围
	# k: 表示还可以添加到列表的个数，所以每dfs一次要减一
	# start：表示开始的数字，所以每dfs一次要+1，不能是小于当前数字的值，防止重复
	# lst: 当前组合
	# ans: 保存最终答案

def main():
	n = int(input("n = "))
	k = int(input("k = "))
	ans = []
	dfs(n, k, 1, [], ans)
	print(ans)

if __name__=="__main__":
	main()






