class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        r = [0] * n
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if r[j] == 0:
                    j = n
                    break
                j += r[j]
            
            if j < n:
                r[i] = j - i
        return r