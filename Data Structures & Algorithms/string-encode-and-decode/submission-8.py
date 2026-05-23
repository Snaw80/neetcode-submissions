class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            l = str(len(string))
            s += f'{l}_{string}'
        return s

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '_':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            r.append(s[i:j])
            i = j
        
        return r