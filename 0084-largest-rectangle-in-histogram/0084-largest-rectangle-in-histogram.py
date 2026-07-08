class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)+1):
            current = 0 if i == (len(heights)) else heights[i]
            while stack and current < heights[stack[-1]]:
                prevheight = heights[stack.pop()]
                width = i if not stack else (i-stack[-1]-1)
                area = width * prevheight
                maxarea = max(area,maxarea)
            stack.append(i)
        return maxarea
        