class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastSeen = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            if s[right] in lastSeen and lastSeen[s[right]] >= left:
                left = lastSeen[s[right]] + 1

            lastSeen[s[right]] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen
