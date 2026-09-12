class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ln = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right

            ln = max(ln, right - left + 1)

        return ln