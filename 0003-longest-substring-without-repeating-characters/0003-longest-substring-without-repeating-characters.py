class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxs = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
            maxs = max(maxs,len(seen))
        return maxs

