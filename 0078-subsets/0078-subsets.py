class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        def sol(index):
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            sol(index+1)
            current.pop()
            sol(index+1)
        sol(0)
        return result            