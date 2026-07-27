class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]: # Check if the newest element in queue is smaller than the current index, if so, remove newest queue element
                q.pop()

            while q and q[0] <= i - k: # i - k is formula for checking leftmost index from left
                q.popleft()

            q.append(i)

            if i >= k - 1: # Check if window formation complete (k elements)
                result.append(nums[q[0]])

        return result

