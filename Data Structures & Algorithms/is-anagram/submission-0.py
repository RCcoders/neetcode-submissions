class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap will be used
        hash1 = {}
        hash2 = {}

        for c in s:
            hash1[c] = hash1.get(c, 0) + 1

        for b in t:
            hash2[b] = hash2.get(b, 0) + 1

        if hash1 == hash2:
            return True
        else:
            return False
