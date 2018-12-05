# -*- coding: utf-8 -*-
# @File 	: 5-2.py
# @Author 	: jianhuChen
# @Date 	: 2018-11-21 16:32:32
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2018-11-21 19:02:21

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

def oddEvenList(L):
	if L != None:
		odd = L # 奇数索引首节点
		even = L.next # 偶数索引首节点
		evenHead = even
		while even != None and even.next != None:
			odd.next = odd.next.next
			even.next = even.next.next
			odd = odd.next
			even = even.next
		odd.next = evenHead
	return L

if __name__ == '__main__':
	L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	L1_head = toList(L1)
	# 转换
	head = oddEvenList(L1_head.next)
	List = []
	getListVal(head, List)
	print("before：",L1)
	print("after ：",List)
