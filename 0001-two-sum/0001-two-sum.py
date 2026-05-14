class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [seen[comp], i]
            seen[nums[i]] = i
        