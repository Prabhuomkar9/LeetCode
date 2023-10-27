class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        ans = []
        products.sort()

        for i in range(len(searchWord)):
            search = searchWord[0 : i + 1]
            l = []
            for product in products:
                if len(l) == 3:
                    break

                if product.startswith(search):
                    l.append(product)
            ans.append(l)

        return ans
