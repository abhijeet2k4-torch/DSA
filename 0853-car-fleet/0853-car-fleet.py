class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tlist = list(zip(position,speed))
        tlist.sort(reverse=True)
        stack = []
        for p,s in tlist:
            steps = (target-p)/s
            if not stack or stack[-1] < steps:
                stack.append(steps)
        return len(stack)