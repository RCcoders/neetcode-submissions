class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case: reached the end of the string
            if i >= len(s):
                res.append(part.copy())
                return

            # Try every possible substring starting from i
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j + 1])

                    dfs(j + 1)

                    # Backtracking
                    part.pop()

        dfs(0)
        return res

    def isPalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True