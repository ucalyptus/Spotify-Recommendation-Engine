class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return other.first == self.first and other.second == self.second

    def __hash__(self):
        a = 1
        b = 1
        if self.first is None:
            a = 0
        if self.second is None:
            b = 0
        if a == 0:
            return hash(self.second)
        if b == 0:
            return hash(self.first)
        if a != 0 and b != 0:
            return hash(self.first) ^ hash(self.second)
        return 0

    @staticmethod
    def create(a, b):
        return Pair(a, b)
