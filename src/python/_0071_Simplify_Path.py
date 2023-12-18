class Solution:
    def simplifyPath(self, path: str) -> str:
        dq = deque()

        for ele in path.split("/"):
            if ele == "..":
                if dq:
                    dq.pop()
            elif ele != "" and ele != ".":
                dq.append(ele)

        return "/" + "/".join(dq)
