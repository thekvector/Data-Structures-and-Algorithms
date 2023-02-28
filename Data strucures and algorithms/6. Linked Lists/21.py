"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

"""
Intuition:
Do merge sort on the linked lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        empty = ListNode()
        l1, l2 = list1, list2
        cur = empty
        while l1 and l2:
            if l1.val< l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return empty.next

s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(4)
h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)
s.mergeTwoLists(h1,h2)