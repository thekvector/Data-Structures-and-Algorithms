"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

"""
Intuition:
Have two pointers. Create a gap between the pointers that equals to 'n'. iterate through list. once the lead pointer reaches the end, we know the follow pointer is at the n'th position. remove it from the list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        h1 = head
        for i in range(n):
            h1 = h1.next
        if not h1:
            return head.next
        prev = None
        h2 = head
        while h1:
            prev = h2
            h1 = h1.next
            h2 = h2.next
        prev.next = h2.next
        return head

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
s.removeNthFromEnd(h, 2)