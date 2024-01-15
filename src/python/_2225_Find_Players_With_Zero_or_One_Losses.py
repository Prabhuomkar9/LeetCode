class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = defaultdict(int)
        winners = set()
        losers = set()

        for w, l in matches:
            lost[l] += 1
            winners.add(w)

        for k, v in lost.items():
            if k in winners:
                winners.remove(k)
            if v == 1:
                losers.add(k)

        return [list(sorted(winners)), list(sorted(losers))]
