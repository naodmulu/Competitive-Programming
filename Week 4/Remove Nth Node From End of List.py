# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        f = node
        s = node
        for i in range(n+1):
            f = f.next
        while f:
            f = f.next
            s = s.next
        s.next = s.next.next
        return node.next