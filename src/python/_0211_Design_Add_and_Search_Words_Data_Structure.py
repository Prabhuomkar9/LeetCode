class WordDictionary:
    def __init__(self):
        self.trie = {"#": True}

    def addWord(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {"#": False}

            curr = curr[c]

        curr["#"] = True

    def search(self, word: str) -> bool:
        def dps(start, trie):
            curr = trie

            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr:
                        if child == "#":
                            continue
                        if dps(i + 1, curr[child]):
                            return True
                    return False
                else:
                    if c not in curr:
                        return False
                    curr = curr[c]

            return curr.get("#")

        return dps(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
