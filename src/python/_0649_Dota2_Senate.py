class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rAlive = 0
        dAlive = 0
        guys = deque()

        for guy in senate:
            guys.append(guy)
            if guy == "R":
                rAlive += 1
            else:
                dAlive += 1

        rToKill = 0
        dToKill = 0
        while rAlive > 0 and dAlive > 0:
            currentGuy = guys.popleft()
            if currentGuy == "R":
                if rToKill > 0:
                    rToKill -= 1
                    rAlive -= 1
                else:
                    dToKill += 1
                    guys.append(currentGuy)
            else:
                if dToKill > 0:
                    dToKill -= 1
                    dAlive -= 1
                else:
                    rToKill += 1
                    guys.append(currentGuy)

        return "Radiant" if rAlive > 0 else "Dire"
