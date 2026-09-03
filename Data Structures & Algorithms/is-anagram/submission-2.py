class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap will be used
        if len(s) != len(t):
            return False
        counts = {}
        for char_s, char_t in zip(s, t):
            counts[char_s] = counts.get(char_s, 0) + 1
            counts[char_t] = counts.get(char_t, 0) - 1

        return all(counts == 0 for counts in counts.values())

