# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        i = len(nodes) - n

        # Removing the head
        if i == 0:
            return head.next

        # Removing the tail
        if i == len(nodes) - 1:
            nodes[i - 1].next = None
        else:
            # Removing a middle node
            nodes[i - 1].next = nodes[i + 1]

        return head

