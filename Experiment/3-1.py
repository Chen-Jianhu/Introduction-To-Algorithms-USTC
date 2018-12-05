#coding=utf-8
# File    : 3-1.py
# Desc    : Remove all elements from a linked list of
#           integers that have value val.
# Author  : jianhuChen
# license : Copyright(C), USTC
# Time    : 2018/10/30 20:48

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initial(head):
	head = ListNode(0)
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(6)
	n4 = ListNode(3)
	n5 = ListNode(4)
	n6 = ListNode(5)
	n7 = ListNode(6)
	head.next = n1
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	return head

def removeElements(head, val):
	pre, cur = head, head.next
	while cur:
		if cur.val == val:
			pre.next = cur.next
		else:
			pre = cur
		cur = cur.next
	return head.next


def getList(node, List):
	if node != None:
		List.append(node.val)
		getList(node.next, List)

if __name__ == '__main__':
	head = ListNode(0)
	head = initial(head)

	List = []
	getList(head.next, List)
	print(List)

	# 删除节点
	head = removeElements(head, 6)
	List = []
	getList(head, List)
	print(List)