class Solution:
    def rob(self, nums: List[int]) -> int:
        hm = {}

        def rec(i):
            if i >= len(nums) - 1:
                if i == len(nums) - 1:
                    return nums[i]
                return 0
            
            else:
                if i not in hm:
                    hm[i] = max(nums[i] + rec(i+2), nums[i+1] + rec(i+3))
                return hm[i]
        
        return rec(0)