class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        m = nums[0]

        for i in range(1,len(nums)):
            if s < 0:
                s = 0
            s += nums[i]
            m = max(s,m)
        return m

