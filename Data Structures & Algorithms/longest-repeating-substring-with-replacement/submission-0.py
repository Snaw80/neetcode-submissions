class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        h = {}
        m = 0
        r = 0
        for right in range(len(s)):
            h[s[right]] = h.get(s[right],0) + 1
            m = max(m,h[s[right]])
            while right - left + 1 - m > k:
                h[s[left]] -= 1
                left += 1
            r = max(r, (right - left) + 1)
        
        return r