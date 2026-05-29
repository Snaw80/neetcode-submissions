class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        for i in range(len(nums)):
            target = -nums[i]
            s,e = 0, len(nums) - 1
            while s<e:
                current = nums[s] + nums[e]
                if s == i or current < target:
                    s += 1
                elif e == i or current > target:
                    e -= 1
                else:
                    new = [nums[i],nums[s],nums[e]]
                    new.sort()
                    if new not in r:
                        r.append(new)
                    e -= 1
                    s += 1
        
        return r