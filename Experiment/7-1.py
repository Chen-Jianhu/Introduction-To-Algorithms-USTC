# -*- coding: utf-8 -*-
# @File 	: 7-1.py
# @Author 	: jianhuChen
# @Date 	: 2018-12-05 12:31:48
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-12-05 12:48:40

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

def construct_maximum_binary_tree(nums):
    if not nums: #递归终点
        return None
    i = nums.index(max(nums)) # 找到最大数量的索引
    node = TreeNode(nums[i]) # 建立节点
    # 以i索引为分界线，一分为二
    node.left = construct_maximum_binary_tree(nums[:i])
    node.right = construct_maximum_binary_tree(nums[i + 1:])
    return node

def main():
	nums = [3, 2, 1, 6, 0, 5]
	head = construct_maximum_binary_tree(nums)
	listTree=[]
	head.getListFromTree(listTree)
	print(listTree)

if __name__ == '__main__':
	main()

# 我们来看看算法的前几个步骤。
# 数组中的最大数字6，存在于索引处3。
# 左子阵列（来自索引0 -> 2）的最大数量是3。
# 右子阵列中的最大数量（来自索引4 -> 5）是5。
# 根节点6和左，右的孩子3和5分别。
# 我们可以在左右子阵列上重复相同的算法，直到数组为空。

# 因此，我们得到以下算法：
# 1. 检查是否nums为空。如果是，请返回None。这可能会形成我们树的叶子。
# 2. 找到最大数量的索引。让我们说它在索引处i。
# 3. 创建一个内部元素为的节点nums[i]。
# 4. 使用nums[:i]右侧子树递归左侧子树nums[i + 1:]。
# 5. 返回节点。