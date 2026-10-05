class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node,count):
            if count == len(word):
                return node.end
            char = word[count]
            if char != ".":
                if char not in node.children:
                    return False
                return dfs(node.children[char],count+1)
            else:
                for ch in node.children.values():
                    if dfs(ch,count+1):
                        return True
                return False

        return dfs(self,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)