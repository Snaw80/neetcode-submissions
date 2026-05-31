class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target-p)/s for p,s in sorted(zip(position,speed))]

        stack = [times[-1]]

        for i in range(len(times)-2,-1,-1):
            if stack[-1] < times[i]:
                stack.append(times[i])
        return len(stack)