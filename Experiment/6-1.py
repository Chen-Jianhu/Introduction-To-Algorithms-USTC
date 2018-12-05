# -*- coding: utf-8 -*-
# @File 	: 6-1.py
# @Author 	: jianhuChen
# @Date 	: 2018-11-27 19:09:27
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-11-27 20:23:57

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x=0):
		self.val = x
		self.left = None;
		self.right = None;
	# 将树转换为先序列表
	def getListFromTree(self, listTree):
		listTree.append(self.val)
		if self.left:
			self.left.getListFromTree(listTree)
		if self.right:
			self.right.getListFromTree(listTree)

# 定义一棵树，供后面测试用
def init_tset():
	# 第一棵树
	tree1 = TreeNode(1)
	Node1_1 = TreeNode(3)
	Node1_2 = TreeNode(2)
	Node1_3 = TreeNode(5)
	tree1.left = Node1_1
	tree1.right = Node1_2
	Node1_1.left = Node1_3
	# 第二棵树
	tree2 = TreeNode(2)
	Node2_1 = TreeNode(1)
	Node2_2 = TreeNode(3)
	Node2_3 = TreeNode(4)
	Node2_4 = TreeNode(7)
	tree2.left = Node2_1
	tree2.right = Node2_2
	Node2_1.right = Node2_3
	Node2_2.right = Node2_4
	return tree1, tree2

# 方法一：使用递归
def mergeTrees(t1, t2):
	if t1 == None: # 若t1为空，则返回t2的地址，此时若t2也为空，则最后该节点的位置为空
		return t2
	if t2 == None: # 若t2为空，则返回t1地址
		return t1
	t1.val += t2.val # 若两者都不为空，将t1的值改为他们的和
	t1.left = mergeTrees(t1.left, t2.left)
	t1.right = mergeTrees(t1.right, t2.right)
	return t1

# Complexity Analysis
# Time complexity : O(m). A total of m nodes need to be traversed. Here, mm represents the minimum number of nodes from the two given trees.
# Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm).

# 测试
def main():
	t1, t2= init_tset()
	t1 = mergeTrees(t1, t2)
	listTree = []
	t1.getListFromTree(listTree)
	print("先序遍历:", listTree)

if __name__ == '__main__':
	main()

# 第二个迭代的方法可以看看下方的参考资料链接