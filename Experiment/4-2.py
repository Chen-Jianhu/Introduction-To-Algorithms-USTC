#coding=utf-8
# File    : 4-2.py
# Desc    : Given a non-empty, singly linked list with head
#			node head, return a middle node of linked list.
# 			If there are two middle nodes, return the second
#			middle node.
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/11/14 12:43

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def toList(L):
	Nodes = [ListNode(0)]
	for x in L:
		Nodes.append(ListNode(int(x)))
	for i in range(len(Nodes)-1):
		Nodes[i].next = Nodes[i+1]
	return Nodes[0]

if __name__ == '__main__':
	L = input("Input L:").split()
	print(L[int(len(L)/2)])		# 方法1

	L_head = toList(L) 			# 方法2

	P1 = L_head.next
	p2 = L_head.next
	
	while P1 != None and P1.next != None:
		P1 = P1.next.next
		p2 = p2.next

	print(p2.val)