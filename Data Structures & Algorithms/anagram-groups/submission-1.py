class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for string in strs:
            c = [0] * 26
            for ch in string:
                c[ord(ch) - ord('a')] += 1
            hm[tuple(c)].append(string)
        
        return list(hm.values())