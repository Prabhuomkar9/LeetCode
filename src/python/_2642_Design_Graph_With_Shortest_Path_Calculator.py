class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            self.graph[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.graph[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        cost = [float("inf") for _ in range(self.n)]
        cost[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heappop(pq)

            if u == node2:
                return cost[node2]

            if d > cost[u]:
                continue

            for v, c in self.graph[u]:
                if cost[u] + c < cost[v]:
                    cost[v] = cost[u] + c
                    heappush(pq, (cost[v], v))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
