class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1 / value

        def dfs(u, v, seen):
            if v in graph[u]:
                return graph[u][v]

            for key, value in graph[u].items():
                if key not in seen:
                    seen.add(u)
                    val = dfs(key, v, seen)
                    if val > 0:
                        return value * val
                    seen.remove(u)

            return -1

        ans = []

        for u, v in queries:
            if u not in graph or v not in graph:
                ans.append(-1)
            else:
                ans.append(dfs(u, v, set()))

        return ans
