class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '[':']', '{':'}'}
        stack = []
        for ch in s:
            if ch in parentheses.keys():
                stack.append(ch)
            elif ch in parentheses.values():
                if not len(stack):
                    return False
                oP = stack.pop()
                if parentheses[oP] != ch:
                    return False
        return len(stack) == 0
