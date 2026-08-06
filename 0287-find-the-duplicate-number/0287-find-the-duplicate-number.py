class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        emptyset = set()
        for n in nums:
            if n in emptyset:
                return n
            emptyset.add(n)

        