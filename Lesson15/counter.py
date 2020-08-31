class Counter:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.current = self.minimum

    def count(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        else:
            return 'Out of range'


res = Counter(24, 30)
print(res.count())
print(res.count())
print(res.count())
print(res.count())
print(res.count())
print(res.count())
print(res.count())
