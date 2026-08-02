class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of = True

    def search(self, word: str) -> bool:

        def dfs(index, node):

            # Base Case
            if index == len(word):
                return node.is_end_of

            char = word[index]

            # Wildcard '.'
            if char == ".":

                for child in node.children.values():

                    if dfs(index + 1, child):
                        return True

                return False

            # Normal Character
            if char not in node.children:
                return False

            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)