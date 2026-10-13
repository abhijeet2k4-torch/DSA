class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current = []
        def sol(current,index):
            if sum(current) > target:
                return
            if sum(current) == target:
                result.append(current.copy())
                return
            for i in range(index,len(candidates)):
                current.append(candidates[i])
                sol(current,i)
                current.pop()
        sol([],0)
        return result