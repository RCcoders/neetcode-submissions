class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, s):
            if s == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or word[s] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, s + 1) or dfs(r - 1, c, s + 1) or dfs(r, c + 1, s + 1) or dfs(r, c - 1, s + 1))
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True

        return False

        

