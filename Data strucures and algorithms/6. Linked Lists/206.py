"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

"""
Intuition:
Have a current, previous and next pointer. While the current pointer exists, have next equal the next of current pointer. Have the next value of current pointer equal previous now. Then make previous equal current. And then finally make current equal the 
next that we stores at the start.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        cur, prev, next = head, None, None
        while cur:
            next = cur.next
            cur.next = prev
            prev= cur
            cur = next
        return prev

head = ListNode(1)
head.next = ListNode(2)
s = Solution()
s.reverseList(head)