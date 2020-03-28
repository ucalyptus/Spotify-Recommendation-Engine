class Rating:
    def __init__(self, userId=None, itemId=None, score=None, timestamp=None, line=None):
        if line is not None:
            arr = line.split('\t')
            self.userId = int(arr[0])
            self.itemId = int(arr[1])
            self.score = float(arr[2])
            if len(arr) > 3:
                self.timestamp = long(arr[3])
        else:
            self.userId = userId
            self.itemId = itemId
            self.score = score
            self.timestamp = timestamp

    def __str__(self):
        return '<' + self.userId + ',' + self.score + ',' + self.timestamp + '>'


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


class DataMap:
    __serialVersionUID = 8001

    def __init__(self, capacity=None):
        self.map = {}
        if capacity is not None:
            self.map = dict.fromkeys(range(capacity), [])

    def get(self, key):
        return self.map[key]

    def put(self, key, value):
        if value is None:
            del self.map[key]
        else:
            self.map[key] = value

    def remove(self, key):
        return self.map.pop(key)

    def contains(self, key):
        if key in self.map:
            return True
        return False

    def itemCount(self):
        return len(self.map)

    def iterator(self):
        return iter(self.map)



