class BrowserHistory:
    def __init__(self, homepage: str):
        self.past = deque([homepage])
        self.future = deque()

    def visit(self, url: str) -> None:
        self.past.append(url)
        self.future = deque()

    def back(self, steps: int) -> str:
        while len(self.past) > 1 and steps > 0:
            self.future.append(self.past.pop())
            steps -= 1

        return self.past[-1]

    def forward(self, steps: int) -> str:
        while len(self.future) > 0 and steps > 0:
            self.past.append(self.future.pop())
            steps -= 1

        return self.past[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
