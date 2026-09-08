class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        best = 0
        r = 0
        for n in nums:
            count[n] += 1
            if best < count[n]:
                best = count[n]
                r = n
                if best >= len(nums)/2:
                    return r
        return r