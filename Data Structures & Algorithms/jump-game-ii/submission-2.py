class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        s = 0
        while r < len(nums) -1 :
            m = l + nums[l]
            for i in range(l+1,r+1):
                m = max(i + nums[i],m)
            l = r + 1
            r = m
            s += 1
        return s