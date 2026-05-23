from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        
        for string in strs:
            c = Counter(string)
            h = [0] * 26
            for k in c.keys():
                h[ord('a')-ord(k)] = c[k]
            h = tuple(h)

            if hm.get(h,None) != None:
                hm[h].append(string)
            else:
                hm[h] = [string]
        
        return [v for v in hm.values()]