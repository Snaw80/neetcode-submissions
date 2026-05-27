class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        r = 0
        for elt in s:
            if (elt - 1) not in s:
                i = 1
                while elt + i in s:
                    i += 1
                if i > r:
                    r = i
        return r