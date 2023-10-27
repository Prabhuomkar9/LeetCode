class Trie:
    def __init__(self, li):
        self.trie = {"#": []}
        for ele in li:
            self.insert(ele)

    def insert(self, word):
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {"#": []}
            if len(curr[c]["#"]) < 3:
                curr[c]["#"].append(word)
            curr = curr[c]

    def search(self, prefix):
        curr = self.trie

        for c in prefix:
            if c not in curr:
                return []
            curr = curr[c]

        return curr["#"]


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        ans = []
        products.sort()

        t = Trie(products)

        for i in range(len(searchWord)):
            search = searchWord[0 : i + 1]
            ans.append(t.search(search))

        return ans
