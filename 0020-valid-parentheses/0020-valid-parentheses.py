class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dictionary = {"}":"{",")":"(","]":"["}
        for char in s:
            if char in dictionary:
                if not stack or stack[-1] != dictionary[char]:
                    return False
                stack.pop() 
            else:
                stack.append(char)
        return not stack
        

