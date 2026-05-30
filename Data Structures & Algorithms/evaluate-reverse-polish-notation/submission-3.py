class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}
        for token in tokens:
            if token in op:
                a = stack.pop()
                b = stack.pop()
                match token:
                    case '+':
                        stack.append(b+a)
                    case '-':
                        stack.append(b-a)
                    case '*':
                        stack.append(b*a)
                    case '/':
                        stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack.pop()