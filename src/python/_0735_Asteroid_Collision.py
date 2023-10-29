class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            finished = False

            while not finished:
                if asteroid > 0 or not stack or stack[-1] < 0:
                    stack.append(asteroid)
                    finished = True
                elif -asteroid < stack[-1] or abs(asteroid) == abs(stack.pop()):
                    finished = True

        return stack
