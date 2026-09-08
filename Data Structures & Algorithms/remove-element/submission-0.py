class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rmv = 0
        i = 0
        while i < len(nums) - rmv:
            if nums[i] == val:
               rmv += 1
               nums[i] = nums[-rmv]
            else:
                i += 1
        
        return len(nums)-rmv
            