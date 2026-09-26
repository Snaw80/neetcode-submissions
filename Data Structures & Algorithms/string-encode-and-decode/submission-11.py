
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + '#' + string

        return encoded

    def decode(self, s: str) -> List[str]:
        n = 0
        r = []
        current = ""
        for ch in s:
            if n:
                current += ch
                n -= 1
                if n == 0:
                    r.append(current)
                    current = ""
            else:
                if ch == '#':
                    n = int(current)
                    if n == 0:
                        r.append("")
                    current = ""
                else:
                    current += ch
        return r
