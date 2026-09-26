from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)

        for ch in s:
            hm1[ch] += 1

        for ch in t:
            hm2[ch] += 1

        print(hm1,hm2)

        return hm1 == hm2