class Solution:
    def isPathCrossing(self, path: str) -> bool:
        move = {
            "N": lambda p: (p[0], p[1] + 1),
            "S": lambda p: (p[0], p[1] - 1),
            "E": lambda p: (p[0] + 1, p[1]),
            "W": lambda p: (p[0] - 1, p[1])
        }

        pos = (0, 0)
        memory = {pos}

        for direction in path:
            pos = move[direction](pos)

            if pos in memory:
                return True

            memory.add(pos)

        return False
