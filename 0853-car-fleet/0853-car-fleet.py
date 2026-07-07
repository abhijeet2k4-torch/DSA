class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tlist = list(zip(position,speed))
        tlist.sort(reverse=True)
        count = 0
        current_steps = 0
        for p,s in tlist:
            steps = float(target - p) / s
            if current_steps < steps:
                count += 1
                current_steps = steps
        return count
