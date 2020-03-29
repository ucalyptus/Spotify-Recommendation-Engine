import numpy as np
import statistics


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
    _serialVersionUID = 8001

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


class DenseVector:
    _serialVersionUID = -2930574547913792430

    def __init__(self, size=None, array=None, deep=None, vec=None):
        if size is not None:
            self.size = size
            self.data = []
        elif array is not None and deep is None:
            DenseVector(array, True)
        elif array is not None and deep is not None:
            self.size = len(array)
            self.data = []
            if deep:
                self.data = [array[i] for i in range(0, self.size)]
            else:
                self.data = array
        elif vec is not None:
            DenseVector(vec.data)

    def clone(self):
        return DenseVector(self)

    def size(self):
        return self.size

    def init(self, mean=None, sigma=None, range=None):
        if range is None and mean is not None and sigma is not None:
            self.data = np.random.normal(mean, sigma, self.size)
        elif range is not None and mean is None and sigma is None:
            self.data = np.random.uniform(low=0, high=range, size=self.size)
        elif range is None and mean is None and sigma is None:
            self.data = np.random.uniform(low=0, high=1, size=self.size)

    def get(self, idx):
        return self.data[idx]

    def getData(self):
        return self.data

    def mean(self):
        return statistics.mean(self.data)

    def sum_data(self):
        return sum(self.data)

    def squaredSum(self):
        return sum(map(lambda i: i * i, self.data))

    def set(self, idx, val):
        self.data[idx] = val

    def setAll(self, val):
        self.data = [val] * self.size

    def add(self, idx, val):
        self.data[idx] += val

    def minus(self, idx, val):
        self.data[idx] -= val

    def addDense(self, val, vec):
        if vec is None and val is not None:
            result = DenseVector(self.size)
            result.data = [(self.data[i] + val) for i in range(self.size)]
            return result
        elif vec is not None and val is None:
            self.size = vec.size
            result = DenseVector(self.size)
            result.data = [(self.data[i] + vec.data[i]) for i in range(result.size)]
            return result

    def minusDense(self, val=None, vec=None):
        if vec is None and val is not None:
            result = DenseVector(self.size)
            result.data = [(self.data[i] - val) for i in range(self.size)]
            return result
        elif vec is not None and val is None:
            self.size = vec.size
            result = DenseVector(self.size)
            result.data = [(self.data[i] - vec.data[i]) for i in range(result.size)]
            return result

    def scale(self, val):
        result = DenseVector(self.size)
        result.data = [(self.data[i] * val) for i in range(self.size)]
        return result

    def selfScale(self, val):
        self.data = [self.data[i] * val for i in range(self.size)]

    def selfAdd(self, vec):
        self.size = vec.size
        self.data = [self.data[i] + vec.data[i] for i in range(vec.size)]

    def inner(self, vec):
        self.size = vec.size
        result = 0
        for i in range(vec.size):
            result += self.get(i) * vec.get(i)
        return result

    def outer(self, vec):
        mat = DenseMatrix(self.size, vec.size)
        for i in range(mat.numRows):
            for j in range(mat.numColumns):
                mat.set(i, j, self.get(i) * vec.get(j))
        return mat

    def __str__(self):
        return str(self.data)
