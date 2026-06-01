class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e = 0,len(nums) - 1

        while s <= e:
            i = (s+e)//2
            elt = nums[i]

            if elt == target:
                return i
            elif elt > target:
                e = i - 1
            else:
                s = i +1 
        return -1