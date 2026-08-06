class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        answers = []
        for i in range(len(nums)):
            while d and d[0] <= i-k:
                d.popleft()
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if i >= k-1:
                answers.append(nums[d[0]])  
        return answers
            