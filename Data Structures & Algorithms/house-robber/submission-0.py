class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            if len(nums) == 1:
                return nums[0]
            return max(nums[0],nums[1])

        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        for i in range(1,len(nums)):
            arr[i] = max(arr[i-1],arr[i-2] + nums[i])
        
        return arr[-1]