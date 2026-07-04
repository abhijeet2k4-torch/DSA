class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kcount = 0
        kindex = deque()
        left = 0
        max_length = 0
        for i in range(len(nums)):
                if kcount == k:
                    break
                if nums[i] == 0:
                    nums[i] = 1
                    kcount += 1
                    kindex.append(i)
        for right in range(len(nums)):
            if nums[right] == 0 and kindex:
                left = kindex[0] +1
                kindex.popleft()
                nums[right] = 1
                kindex.append(right)
            if nums[right] == 0 and not kindex:
                left = right+1
            max_length = max(max_length,(right-left+1))
        return max_length





