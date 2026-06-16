class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def rec(idx,curr, total):
            if target == total:
                res.append(curr.copy())
            
            i = idx
            while i < len(nums) and total + nums[i] <= target:
                rec(i,curr + [nums[i]],total + nums[i])
                i += 1

        
        rec(0,[],0)
        return res