class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remain = k
        kcount = 0
        kindex = deque()
        left = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0 and k == 0:
                left = right+1
            if nums[right] == 0 and remain>0:
                nums[right] = 1
                remain -= 1
                kindex.append(right)
            if nums[right] == 0 and remain == 0 and k != 0:
                nums[right] = 1
                left = kindex[0]+1
                kindex.popleft()
                kindex.append(right)
            max_length = max(max_length,(right-left+1))
        return max_length





