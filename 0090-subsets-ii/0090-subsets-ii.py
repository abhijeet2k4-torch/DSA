class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        current = []
        def sol(index):
            if index == len(nums):
                result.append(current.copy())
                return 
            current.append(nums[index])
            sol(index+1)
            current.pop()
            i = index+1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
            sol(i) 
        sol(0)
        return result
        