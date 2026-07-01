class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for n in asteroids:
            if n<0:
                    while stack and stack[-1] > 0 and stack[-1]<abs(n):
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(n)
                    elif (stack[-1]+n) == 0:
                        stack.pop()
                    
            else:
                stack.append(n)     
        return stack           
                    

