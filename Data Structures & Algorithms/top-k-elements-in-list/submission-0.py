from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]

        for key,value in count.items():
            freq[value].append(key)

        r = []
        for i in range(len(freq) - 1, 0, -1):
            for elt in freq[i]:
                r.append(elt)
                if len(r) == k:
                    return r