class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxs = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[right] in set(s[left:right]):
                while s[right] in set(s[left:right]):
                    left += 1
                right+= 1
            else:
                right+=1
            maxs = max(maxs,len(set(s[left:right])))
        return maxs

