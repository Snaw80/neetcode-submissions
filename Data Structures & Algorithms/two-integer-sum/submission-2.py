class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = i
        
        for i in range(len(nums)):
            t = hm.get(target-nums[i],None)
            if t != None and i != t:
                return [i,t]
        
        return []