class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = set()
        current = []
        def sol():
            if len(current) == len(nums):
                result.append(current.copy())
                return
            for i in range(len(nums)):
                element = nums[i]
                if element not in used:
                    current.append(element)
                    used.add(element)
                    sol()
                    current.pop()
                    used.remove(element)
        sol()
        return result