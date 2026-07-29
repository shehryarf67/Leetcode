"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        copies = {}
        current = head

        # First pass: create a copy of every node
        while current:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass: connect next and random pointers
        while current:
            copiedNode = copies[current]

            copiedNode.next = copies.get(current.next)
            copiedNode.random = copies.get(current.random)

            current = current.next

        return copies[head]

        