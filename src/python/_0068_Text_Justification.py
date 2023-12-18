class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        temp = []
        spaceCount = maxWidth

        for word in words:
            w = len(word)
            if w - (1 if not temp else 0) < spaceCount:
                spaceCount -= w + (1 if temp else 0)
                temp.append(word)
            else:
                n = len(temp) - 1
                spaceCount += n
                result = ""

                for ele in temp:
                    result += ele
                    if spaceCount > 0:
                        k = ceil(spaceCount / n) if n > 0 else spaceCount
                        spaceCount -= k
                        result += " " * k
                    n -= 1

                ans.append(result)

                temp = [word]
                spaceCount = maxWidth - len(word)

        if temp:
            result = " ".join(temp)
            ans.append(result + " " * (maxWidth - len(result)))

        return ans
