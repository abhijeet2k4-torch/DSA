class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        formed = 0
        min_length = float("inf")
        left = 0
        start = 0
        window = defaultdict(int)
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in t and window[s[right]] == need[s[right]]:
                formed += 1
            while formed == required:
                if right-left+1 < min_length:
                    min_length = right-left+1
                    start = left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        return s[start:start+min_length]