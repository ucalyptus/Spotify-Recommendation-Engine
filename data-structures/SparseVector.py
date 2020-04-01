import math


class SparseVector:
    _serialVersionUID = 8002

    def __init__(self, n=None, sv=None):
        if n is None and sv is None:
            self.N = 0
            self.map = DataMap()
        elif n is not None and sv is None:
            self.N = n
            self.map = DataMap()
        else:
            self.N = sv.N
            self.map = DataMap()
            for i in range(self.N):
                self.setValue(i, sv.getValue(i))

    def setValue(self, i, value):
        if value == 0.0:
            self.map.remove(i)
        else:
            self.map.put(i, value)

    def setVector(self, newVector):
        if self.length() != newVector.length():
            raise RuntimeException("Vector length disagrees.")
        indexList = self.indexList()
        for i, _ in enumerate(indexList):
            self.setValue(i, 0)

        indexList = newVector.indexList()
        for i, _ in enumerate(indexList):
            self.setValue(i, newVector.getValue(i))

    def getValue(self, i):
        if self.map.contains(i):
            return self.map.get(i)
        else:
            return 0.0

    def remove(self, i):
        if self.map.contains(i):
            self.map.remove(i)

    def copy(self):
        newVector = SparseVector(self.N)
        for i, _ in enumerate(self.map):
            newVector.setValue(i, self.getValue(i))
        return newVector

    def indexList(self):
        if self.itemCount() == 0:
            return []
        result = []
        for i, _ in enumerate(self.map):
            result.append(i)
        return result

    def indexSet(self):
        s = set()
        if self.itemCount() == 0:
            return s
        for i, _ in enumerate(self.map):
            s.add(i)
        return s

    def initialize(self, value, index=None):
        if index is None:
            for i in range(self.N):
                self.setValue(i, value)

        else:
            for i in range(index.length()):
                self.setValue(index[i], value)

    def length(self):
        return self.N

    def itemCount(self):
        return len(self.map)

    def nonZeroCount(self):
        count = 0
        for i, _ in enumerate(self.map):
            if self.map.get(i) != 0:
                count += 1
        return count

    def setLength(self, n):
        self.N = n

    def add(self, alpha):
        a = self
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, alpha + a.getValue(i))
        return c

    def sub(self, alpha):
        a = self
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, a.getValue(i) - alpha)
        return c

    def scale(self, alpha):
        a = self
        c = SparseVector(self.N)
        if alpha == 0:
            return c
        for i, _ in enumerate(a.map):
            c.setValue(i, alpha * a.getValue(i))

    def selfScale(self, alpha):
        a = self
        for i, _ in enumerate(a.map):
            a.setValue(i, alpha * a.getValue(i))
        return a

    def power(self, alpha):
        a = self
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, a.getValue(i) ** alpha)
        return c

    def exp(self, alpha):
        a = self
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, alpha ** a.getValue(i))
        return c

    def log2(self, n=None):
        if n is not None:
            return math.log(n) / math.log(2)
        else:
            c = SparseVector(self.N)
            for i, _ in enumerate(a.map):
                c.setValue(i, 1 + self.log2(self.getValue(i)))
            return c

    @staticmethod
    def makeUniform(n):
        v = SparseVector(n)
        val = 1 / n
        for i in range(n):
            v.setValue(i, val)
        return v

    @staticmethod
    def makeRandom(m):
        a = SparseVector(m)
        for i in range(m):
            a.setValue(i, math.random())
        return a

    @staticmethod
    def cosineSimilarity(a, b):
        if a.itemCount() == 0 or b.itemCount() == 0:
            return 0
        innerProduct = a.innerProduct(b)
        if innerProduct == 0:
            return 0
        else:
            return math.sqrt(a.squareSum()) * math.sqrt(b.squareSum())

    def norm(self):
        a = self
        return math.sqrt(a.innerProduct(a))

    def L1_norm(self):
        sum = self.sum()
        return self.scale(1 / sum)

    def sum(self):
        a = self
        sum = 0.0
        for i, _ in enumerate(a.map):
            sum += a.getValue(i)
        return sum

    def squareSum(self):
        return self.innerProduct(self)

    def max(self):
        a = self
        curr = a.getValue(0)
        for i, _ in enumerate(a.map):
            if a.getValue(i) > curr:
                curr = a.getValue(i)
        return curr

    def min(self):
        a = self
        curr = a.getValue(0)
        for i, _ in enumerate(a.map):
            if a.getValue(i) < curr:
                curr = a.getValue(i)
        return curr

    def absoluteSum(self):
        a = self
        sum = 0.0
        for i, _ in enumerate(a.map):
            sum += abs(a.getValue(i))
        return sum

    def average(self):
        a = self
        return a.sum() / (a.itemCount())

    def variance(self):
        avg = self.average()
        sum = 0.0
        for i, _ in enumerate(a.map):
            sum += (self.getValue(i) - avg) ** 2
        return sum / self.itemCount()

    def stdev(self):
        return math.sqrt(self.variance())

    def plus(self, b):
        a = self
        if a.N != b.N:
            raise RuntimeException("Vector lengths disagree")
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, a.getValue(i))
        for i, _ in enumerate(b.map):
            c.setValue(i, b.getValue(i) + c.getValue(i))
        return c

    def selfPlus(self, b):
        a = self
        if a.N != b.N:
            raise RuntimeException("Vector lengths disagree")
        for i, _ in enumerate(b.map):
            a.setValue(i, a.getValue(i) + b.getValue(i))
        return a

    def minus(self, b):
        a = self
        if a.N != b.N:
            raise RuntimeException("Vector lengths disagree")
        c = SparseVector(self.N)
        for i, _ in enumerate(a.map):
            c.setValue(i, a.getValue(i))
        for i, _ in enumerate(b.map):
            c.setValue(i, c.getValue(i) - b.getValue(i))
        return c

    def selfMinus(self, b):
        a = self
        if a.N != b.N:
            raise RuntimeException("Vector lengths disagree")
        for i, _ in enumerate(b.map):
            a.setValue(i, a.getValue(i) - b.getValue(i))
        return a

    def commonMinus(self, b):
        a = self
        c = SparseVector(self.N)
        if a.itemCount() <= b.itemCount():
            for i, _ in enumerate(a.map):
                if b.map.contains(i):
                    c.setValue(i, a.getValue(i) - b.getValue(i))
        else:
            for i, _ in enumerate(b.map):
                if a.map.contains(i):
                    c.setValue(i, a.getValue(i) - b.getValue(i))
        return c

    def innerProduct(self, b):
        a = self
        sum = 0.0

        if a.N != b.N:
            raise RuntimeException("Vector lengths disagree")

        if a.itemCount() <= b.itemCount():
            for i, _ in enumerate(a.map):
                if b.map.contains(i):
                    sum += a.getValue(i) * b.getValue(i)
        else:
            for i, _ in enumerate(b.map):
                if a.map.contains(i):
                    sum += a.getValue(i) * b.getValue(i)

        return sum

    def outerProduct(self, b):
        A = SparseMatrix(self.N, b.N)
        for i in range(self.N):
            for j in range(b.N):
                A.setvalue(i, j, self.getValue(i) * b.getValue(j))
        return A

    def dotProduct(self, b):
        if self.N != b.N:
            raise RuntimeException("dotProduct Error - Vector lengths disagree")
        c = SparseVector(self.N)
        for i, _ in enumerate(self.map):
            if getValue(i) != 0 and b.getValue(i) != 0:
                c.setValue(i, getValue(i) * b.getValue(i))

        return c

    def partPlus(self, b, indexList):
        if indexList == nullptr:
            return self

        if self.N != b.N:
            raise RuntimeException("Vector lengths disagree")

        for i, _ in enumerate(indexList):
            self.setValue(i, self.getValue(i) + b.getValue(i))

        return self

    def partMinus(self, b, indexList):
        if indexList == nullptr:
            return self

        if self.N != b.N:
            raise RuntimeException("Vector lengths disagree")

        for i, _ in enumerate(indexList):
            self.setValue(i, self.getValue(i) - b.getValue(i))

        return self

    def partInnerProduct(self, b, indexList):
        sum = 0.0

        if indexList != nullptr:
            for i, _ in enumerate(indexList):
                sum += self.getValue(i) * b.getValue(i)

        return sum

    def partOuterProduct(self, b, indexList):
        if indexList == null:
            return nullptr
        A = SparseMatrix(b.length(), b.length())

        for i, _ in enumerate(indexList):
            for j, _ in enumerate(indexList):
                A.setValue(i, j, this.getValue(i) * b.getValue(j))

        return A

    def topIndicesByValue(self, topK, ignoreIndices):
        hashmap = {}
        for i, _ in enumerate(self.indexList):
            hashmap[j] = self.getValue(i)
        CommonUtils.TopKeysByValue(hashmap, topK, ignoreIndices)

    def __str__(self):
        s = ""
        for i, _ in enumerate(self.map):
            s += '(' + str(i) + ': ' + str(self.map.get(i)) + ') '
        return s

    def KeysToString(self):
        s = '['
        for i, _ in enumerate(self.map):
            s += str(i) + ', '
        s += ']'
        return s
