# -*- coding: utf-8 -*-
# @File 	: 5-1.py
# @Author 	: jianhuChen
# @Date 	: 2018-11-21 16:32:11
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-11-21 20:45:07

from random import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# isRandom：是否随机找一个点循环
def toRandomCycleList(L, isRandom=False, cycleStart=1):
	Nodes = [ListNode(0)]
	for x in L:
		Nodes.append(ListNode(int(x)))
	for i in range(len(Nodes)-1):
		Nodes[i].next = Nodes[i+1]
	if isRandom:
		Nodes[len(Nodes)-1].next = Nodes[randint(1, len(Nodes)-1)]
	else:
		Nodes[len(Nodes)-1].next = Nodes[cycleStart]
	return Nodes[0]

def findCycleStart(head):
	isCycle = False
	fast = head
	slow = head
	while slow != None and fast != None:
		slow = slow.next
		if fast.next == None:
			return None
		fast = fast.next.next
		if slow == fast:
			isCycle = True
			break
	if not isCycle:
		return None
	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return slow

if __name__ == '__main__':
	L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# 将列表转换为链表形式，注意返回的链表带有一个头结点
	# 所以待会儿找循环的起始位置时，传入的链表head应该为L1_head.next
	L1_head = toRandomCycleList(L1, isRandom=True)
	start = findCycleStart(L1_head.next)
	# 如果没有循环则输出None 
	if start:
		print(start.val)
	else:
		print("None")


