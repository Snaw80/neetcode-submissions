class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s,e = 0, len(numbers) - 1
        r = numbers[s] + numbers[e]
        while r != target:
            if r > target:
                e -= 1
            else:
                s += 1
            r = numbers[s] + numbers[e]
        return [s+1,e+1]

        