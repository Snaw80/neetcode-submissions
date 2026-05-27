class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        b = 0
        e = len(s) - 1
        while b < e:
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True