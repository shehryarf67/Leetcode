# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        for i in range(0, len(nodes) - k + 1, k):
            steps = k
            first = i
            last = i + steps - 1

            while first < last:
                nodes[first], nodes[last] = nodes[last], nodes[first]
                first += 1
                last -= 1
                steps -= 1

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None

        return nodes[0]
            