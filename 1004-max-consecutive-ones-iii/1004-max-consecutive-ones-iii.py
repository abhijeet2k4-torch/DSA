class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cz = 0
        maxl = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if cz < k:
                    cz+=1
                else:
                    while nums[left] != 0:
                        left+=1
                    left += 1
            maxl = max(maxl, (right-left+1))
        return maxl
                    





