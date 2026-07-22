class TimeMap(object):

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        history = self.map[key]

        left, right = 0, len(history) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if history[mid][0] <= timestamp:
                result = history[mid][1] # This is the previous value in case there is no value on timestamp
                left = mid + 1
            else:
                right = mid - 1

        return result

            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)