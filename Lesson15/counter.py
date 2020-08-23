class Counter:
    current = 0

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def count(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        else:
            return self.minimum


res = Counter(0, 5)
print(res.count())
print(res.count())
print(res.count())
print(res.count())
print(res.count())
print(res.count())
