class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s

            if not time or t > time[-1]:
                time.append(t)

        return len(time)
