class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        r = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while  len(stack) > 0 and temperatures[stack[-1]] < t:
                elt = stack.pop()
                r[elt] = i - elt
            stack.append(i)
        
        return r