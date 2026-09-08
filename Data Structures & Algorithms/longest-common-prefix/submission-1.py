class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs[1:]:
            i = 0
            while i < len(longest) and i < len(s) and longest[i] == s[i]:
                i += 1
            if not i:
                longest = ""
            longest = longest[:i]
        return longest