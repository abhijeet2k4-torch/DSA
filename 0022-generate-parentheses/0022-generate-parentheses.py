class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        op = 0
        cl = 0
        result = []
        current = ""
        def sol():
            nonlocal op
            nonlocal cl
            nonlocal current
            if op == n and cl == n:
                result.append(current)
                return
            if op < n:
                current+="("
                op += 1
                sol()
                op-=1
                current = current[:-1]
            if cl < op:
                current+=")"
                cl += 1
                sol()
                cl-=1
                current = current[:-1]
        sol()
        return result