#coding=utf-8
# File    : 4-1.py
# Desc    : Merge two sorted linked lists and return it as a
#			new list. The new list should be made by splicing
#			together the nodes of the first two lists.
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/11/14 12:00

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getListVal(node, List):
	if node != None:
		List.append(node.val)
		getListVal(node.next, List)

def toList(L):
	Nodes = [ListNode(0)]
	for x in L:
		Nodes.append(ListNode(int(x)))
	for i in range(len(Nodes)-1):
		Nodes[i].next = Nodes[i+1]
	return Nodes[0]

if __name__ == '__main__':
	L1 = input("L1:").split('->')
	L2 = input("L2:").split('->')
	L1_head = toList(L1)
	L2_head = toList(L2)

	mergeHead = ListNode(0)
	mergeP = mergeHead
	while L1_head.next != None and L2_head.next != None:
		if L1_head.next.val <= L2_head.next.val:
			mergeP.next = L1_head.next
			mergeP = mergeP.next
			L1_head.next = L1_head.next.next
		else:
			mergeP.next = L2_head.next
			mergeP = mergeP.next
			L2_head.next = L2_head.next.next

	while L1_head.next != None:
		mergeP.next = L1_head.next
		mergeP = mergeP.next
		L1_head.next = L1_head.next.next

	while L2_head.next != None:
		mergeP.next = L2_head.next
		mergeP = mergeP.next
		L2_head.next = L2_head.next.next

	List = []
	getListVal(mergeHead.next, List)
	print(List)

