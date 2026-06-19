class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(nums2)
        ans = []
        adict = {}
        for i in range(length-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                adict[nums2[i]] = stack[-1]
            else:
                adict[nums2[i]] = -1
            stack.append(nums2[i])
        for n in nums1:
            ans.append(adict[n])
        return ans

