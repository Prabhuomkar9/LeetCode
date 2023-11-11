class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = candidates
        r = len(costs) - candidates

        left = costs[:l]
        right = costs[max(l, r) :]
        heapify(left)
        heapify(right)
        cost = 0

        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                cost += heappop(left)
                if l < r:
                    heappush(left, costs[l])
                    l += 1
            else:
                cost += heappop(right)
                if l < r:
                    r -= 1
                    heappush(right, costs[r])

        return cost
