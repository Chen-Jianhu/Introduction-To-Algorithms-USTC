# -*- coding: utf-8 -*-
# @File     : 7-2.py
# @Author   : jianhuChen
# @Date     : 2018-12-05 12:48:55
# @License  : Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-12-05 18:49:57

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x=None):
		self.val = x
		self.left = None;
		self.right = None;

# 定义一棵树，供后面测试用
def init_tset():
	tree = TreeNode(3)
	Node1 = TreeNode(9)
	Node2 = TreeNode(20)
	Node3 = TreeNode(15)
	Node4 = TreeNode(7)
	tree.left = Node1
	tree.right = Node2
	Node2.left = Node3
	Node2.right = Node4
	return tree

# 方法一：递归
def maxDepthRecursion(root):
	if root is None: 
		return 0 
	else: 
		left_height = maxDepthRecursion(root.left) 
		right_height = maxDepthRecursion(root.right) 
		return max(left_height, right_height) + 1 

# 方法二:迭代
def maxDepthIteration(root):
	stack = []
	if root is not None:
		stack.append((1, root))
	
	depth = 0
	while stack != []:
		current_depth, root = stack.pop()
		if root is not None:
			depth = max(depth, current_depth)
			stack.append((current_depth + 1, root.left))
			stack.append((current_depth + 1, root.right))
	
	return depth

def main():
	tree = init_tset() # 构造一棵树用于测试

	depth1 = maxDepthRecursion(tree) # 方法一：递归
	depth2 = maxDepthIteration(tree) # 方法二：迭代
	print("maxDepthRecursion:", depth1)
	print("maxDepthIteration:", depth2)

if __name__ == '__main__':
	main()