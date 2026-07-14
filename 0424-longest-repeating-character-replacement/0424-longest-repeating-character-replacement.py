class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        hashs = {}
        maxf = 0
        for right in range(len(s)):
            hashs[s[right]] = hashs.get(s[right],0)+1
            maxf = max(maxf,hashs[s[right]])
            while (right-left+1) - maxf > k:
                hashs[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans
