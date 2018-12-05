#coding=utf-8
# File    : 3-2.py
# Desc    : Given a 2D board and a word, find if the word
# 			exists in the grid. The word can be constructed
# 			from letters of sequentially adjacent cell, where
# 			"adjacent" cells are those horizontally or
# 			vertically neighboring. The same letter cell may
# 			not be used more than once.
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/10/30 21:21

def exist(board, word):
	if len(board) == 0:
		return False
	for i in range(len(board)):
		for j in range(len(board[0])):
			# 从i,j点作为起点开始搜索
			isExisted = search(board, i, j, word, 0)
			if isExisted:
				return True
	return False

def search(board, i, j, word, idx):
	if idx>=len(word):
		return True
	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[idx]:
		return False
	# 将已经搜索过的字母标记一下，防止循环。只要变成另外一个字符，就不会再有循环了。
	temp = board[i][j]
	board[i][j] = '*'
	res = search(board, i-1, j, word, idx+1) or search(board, i+1, j, word, idx+1) \
	      or search(board, i, j-1, word, idx+1) or search(board, i, j+1, word, idx+1)
	# 再次异或255就能恢复成原来的字母
	board[i][j] = temp
	return res

if __name__ == '__main__':
	board = [['A', 'B', 'C', 'E'],
	         ['S', 'F', 'C', 'S'],
	         ['A', 'D', 'E', 'E']]
	flag = exist(board, "SEE")
	print(flag)