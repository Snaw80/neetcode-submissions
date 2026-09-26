class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            if n in hm.keys():
                print(hm)
                return True
            hm[n] = 1

        return False