class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        odict = ("+", "-", "*","/")
        for t in tokens:
            if t not in odict:
                stack.append(t)
            else:
                secondnum = int(stack.pop())
                firstnum = int(stack.pop())
                if t == "+":
                    firstnum = firstnum+secondnum
                elif t == "-":
                    firstnum = firstnum-secondnum
                elif t == "*":
                    firstnum = firstnum*secondnum
                else:
                    firstnum = firstnum/secondnum
                stack.append(firstnum)
        return int(stack[0])