class MinStack:

    def __init__(self):
        self.cache = []
        self.minCache = []

    def push(self, val: int) -> None:
        self.cache.append(val)
        if not self.minCache:
            self.minCache.append(val)
        else:
            self.minCache.append(min(val, self.minCache[-1]))

    def pop(self) -> None:
        self.cache.pop()
        self.minCache.pop()

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        return self.minCache[-1]
