class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        for elt in nums:
            if elt:
                prod *= elt
            else:
                zero += 1

        if zero > 1:
            return [0] * len(nums)
        if zero == 1:
            return [prod if elt == 0 else 0 for elt in nums]

        return [int(prod/elt) for elt in nums]
