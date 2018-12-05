# -*- coding: utf-8 -*-
# @File 	: 6-2.py
# @Author 	: jianhuChen
# @Date 	: 2018-11-27 19:26:27
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-11-28 18:46:06

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x=0):
		self.val = x
		self.left = None
		self.right = None
	# 将树转换为先序列表
	def getListFromTree(self, listTree):
		listTree.append(self.val)
		if self.left:
			self.left.getListFromTree(listTree)
		if self.right:
			self.right.getListFromTree(listTree)

def searchBST(root, val):
	stack = [root] # 栈
	while stack:
		cur = stack.pop()
		if cur.val == val:
			return cur
		if cur.left and cur.val > val: # 含有左孩子，并且待查找关键字比当节点的值小，此时去左边找
			stack.append(cur.left)
		elif cur.right and cur.val < val: # 含有右孩子，并且待查找关键字比当节点的值大，此时去右边找
			stack.append(cur.right)
	return None

# 定义一棵树，供后面测试用
def init_tset():
	tree = TreeNode(4)
	Node1 = TreeNode(2)
	Node2 = TreeNode(7)
	Node3 = TreeNode(1)
	Node4 = TreeNode(3)
	tree.left = Node1
	tree.right = Node2
	Node1.left = Node3
	Node1.right = Node4
	return tree

def main():
	newTree = searchBST(init_tset(), 4)
	listTree = []
	newTree.getListFromTree(listTree)
	print("先序遍历:", listTree)

if __name__ == '__main__':
	main()

