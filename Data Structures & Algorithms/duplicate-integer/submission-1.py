from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return  True in [i != 1 for i in counter.values()]