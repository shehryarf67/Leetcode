class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]: # Because one bucket can contain multiple numbers
                result.append(num)

                if len(result) == k:
                    return result