class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None   # avoid duplicates

            board[r][c] = '#'

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return ans