from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1set = defaultdict(int)
        s2set = defaultdict(int)
        left = 0
        for s in s1:
            s1set[s] += 1
        for right in range(len(s2)):
            s2set[s2[right]] += 1
            if (right-left+1)>len(s1):
                s2set[s2[left]] -= 1
                if s2set[s2[left]] == 0:
                    del s2set[s2[left]]
                left += 1
            if s2set == s1set:
                return True
        return False

