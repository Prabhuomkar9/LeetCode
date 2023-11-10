class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        for u in graph:
            if len(graph[u]) == 1:
                ans = [u, graph[u][0]]
                seen = {u}
                break

        curr = ans[1]
        while curr not in seen:
            seen.add(curr)
            neighbours = graph[curr]
            for neighbour in neighbours:
                if neighbour not in seen:
                    ans.append(neighbour)
                    curr = neighbour
                    break

        return ans
