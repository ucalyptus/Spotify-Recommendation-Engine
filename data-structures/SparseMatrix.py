import math
import random


class SparseMatrix:
    _serialVersionUID = 8003

    def __init__(self, m=None, n=None, sm=None):
        if sm is None:
            self.M = m
            self.N = n
            rows = [] * self.M
            cols = [] * self.N
            for i in range(self.M):
                rows[i] = SparseVector(self.N)
            for j in range(self.N):
                cols[j] = SparseVector(self.M)
        else:
            self.M = sm.M
            self.N = sm.N
            rows = [] * self.M
            cols = [] * self.N
            for i in range(self.M):
                rows[i] = sm.getRow(i)
            for j in range(self.N):
                cols[j] = sm.getCol(j)

    def getValue(self, i, j):
        return self.rows[i].getValue(j)

    def setValue(self, i, j, value):
        if value == 0.0:
            self.rows[i].remove(j)
            self.cols[j].remove(i)
        else:
            self.rows[i].setValue(j, value)
            self.cols[j].setValue(i, value)

    def setRowVector(self, i, newVector):
        if newVector.length() != this.N:
            raise RuntimeException("Vector lengths disagree")
        if i < 0 or i >= self.M:
            raise RuntimeException("Wrong input row index.")
        if rows[i].indexList() is not None:
            for j, _ in enumerate(rows[i].indexList()):
                self.setValue(i, j, 0)
        if newVector.indexList() is not None:
            for j, _ in enumerate(newVector.indexList()):
                self.setValue(i, j, newVector.getValue(j))

    def setRowVectorNonegative(self, newVector):
        if newVector.length() != self.N:
            raise RuntimeException("Vector lengths disagree")
        if i < 0 or i >= self.M:
            raise RuntimeException("Wrong input row index.")
        if rows[i].indexList() is not None:
            for j, _ in enumerate(rows[i].indexList()):
                self.setValue(i, j, 0)
        if newVector.indexList() is not None:
            for j, _ in enumerate(newVector.indexList()):
                value = newVector.getValue(j)
                if value > 0:
                    self.setValue(i, j, value)
                else:
                    self.setValue(i, j, 0)

    def setColVector(self, j, newVector):
        if newVector.length() != self.M:
            raise RuntimeException("Vector lengths disagree")
        if j < 0 or j >= self.N:
            raise RuntimeException("Wrong input column index.")
        if cols[j].indexList() is not None:
            for i, _ in enumerate(cols[j].indexList()):
                this.setValue(i, j, 0)
        if newVector.indexList() is not None:
            for i, _ in enumerate(newVector.indexList()):
                self.setValue(i, j, newVector.getValue(i))

    def setSize(self, m, n):
        self.M = m
        self.N = n

    def getRowRef(self, index):
        return self.rows[index]

    def getRow(self, index):
        newVector = self.rows[index].copy()
        return newVector

    def getColRef(self, index):
        return self.cols[index]

    def getRowAverage(self, defalut_value):
        rowAverage = SparseVector(self.M)
        for u in range(self.M):
            v = self.getRowRef(u)
            avg = v.average()
            if Double.isNaN(avg):
                avg = defalut_value
            rowAverage.setValue(u, avg)
        return rowAverage

    def getColumnAverage(self, defalut_value):
        columnAverage = SparseVector(self.N)
        for i in range(self.N):
            j = self.getColRef(i)
            avg = j.average()
            if Double.isNaN(avg):
                avg = defalut_value
            columnAverage.setValue(i, avg)
        return columnAverage

    def length(self):
        lengthArray = []
        lengthArray[0] = self.M
        lengthArray[1] = self.N
        return lengthArray

    def size(self):
        return self.M * self.N

    def itemCount(self):
        sum = 0
        if self.M > self.N:
            for i in range(self.M):
                sum += rows[i].itemCount()
        else:
            for j in range(self.N):
                sum += cols[j].itemCount()
        return sum

    def nonZeroCount(self):
        sum = 0
        if M > N:
            for i in range(self.M):
                sum += rows[i].nonZeroCount()

        else:
            for j in range(self.N):
                sum += cols[j].nonZeroCount()
        return sum

    def diagonal(self):
        v = SparseVector(min(self.M, self.N))

        for i in range(min(self.M, self.N)):
            value = self.getValue(i, i)
            if value > 0.0:
                v.setValue(i, value)

        return v

    def max(self):
        curr = -999999999999999999999999999999999999
        for i in range(self.M):
            v = self.getRowRef(i)
            if v.itemCount() > 0:
                rowMax = v.max()
                if v.max() > curr:
                    curr = rowMax
        return curr

    def min(self):
        curr = 999999999999999999999999999999999999
        for i in range(self.M):
            v = self.getRowRef(i)
            if v.itemCount() > 0:
                rowMin = v.min()
                if v.min() < curr:
                    curr = rowMin
        return curr

    def sum(self):
        sum = 0.0
        for i in range(self.M):
            v = self.getRowRef(i)
            sum += v.sum()

        return sum

    def squareSum(self):
        sum = 0.0
        for i in range(self.M):
            v = self.getRowRef(i)
            sum += v.squareSum()

        return sum

    def average(self):
        return self.sum() / self.itemCount()

    def variance(self):
        avg = self.average()
        sum = 0.0

        for i in range(self.M):
            itemList = self.getRowRef(i).indexList()
            for j, _ in enumerate(itemList):
                sum += (self.getValue(i, j) - avg) ** 2

        return sum / this.itemCount()

    def stdev(self):
        return math.sqrt(self.variance())

    def indexPairs(self):
        pairs = []
        for i in range(self.M):
            for j in rows[i].indexList():
                p = i, j
                pairs.append(p)
        return pairs

    def scale(self, alpha):
        A = SparseMatrix(self.M, self.N)

        for i in range(A.M):
            A.rows[i] = self.getRowRef(i).scale(alpha)
        for j in range(A.N):
            A.cols[j] = self.getColRef(j).scale(alpha)

        return A

    def selfScale(self, alpha):
        for i in range(self.M):
            itemList = self.getRowRef(i).indexList()
            for j, _ in enumerate(itemList):
                self.setValue(i, j, self.getValue(i, j) * alpha)
        return self

    def add(self, alpha):
        A = SparseMatrix(self.M, self.N)

        for i in range(A.M):
            A.rows[i] = this.getRowRef(i).add(alpha)
        for j in range(A.N):
            A.cols[j] = this.getColRef(j).add(alpha)

        return A

    def selfAdd(self, alpha):
        for i in range(self.M):
            itemList = self.getRowRef(i).indexList()
            for j, _ in enumerate(itemList):
                self.setValue(i, j, self.getValue(i, j) + alpha)

    def exp(self, alpha):
        for i in range(self.M):
            b = self.getRowRef(i)
            indexList = b.indexList()
            for j, _ in enumerate(indexList):
                self.setValue(i, j, Math.pow(alpha, self.getValue(i, j)))

        return self

    def transpose(self):
        A = SparseMatrix(self.N, self.M)
        A.cols = this.rows
        A.rows = this.cols

        return A

    def times(self, x):
        if N != x.length():
            raise RuntimeException("Dimensions disagree")

        A = self
        b = SparseVector(M)

        for i in range(self.M):
            b.setValue(i, A.rows[i].innerProduct(x))

        return b

    def times(self, B):
        # original implementation
        if self.N != (B.length())[0]:
            raise RuntimeException("Dimensions disagree")
        A = self
        C = SparseMatrix(M, (B.length())[1])
        for i in range(self.M):
            for j in range(B.length())[1]:
                x = A.getRowRef(i)
                y = B.getColRef(j)
                if x is not None and y is not None:
                    C.setValue(i, j, x.innerProduct(y))
                else:
                    C.setValue(i, j, 0.0)

        return C

    def dotTimes(self, B):
        if self.M != B.M or self.N != B.N:
            raise RuntimeException("dotTimes: Matrices are not of the same size!")
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            wordList = self.rows[i].indexList()
            for j, _ in enumerate(wordList):
                A_ij = getValue(i, j)
                B_ij = B.getValue(i, j)
                if A_ij != 0 and B_ij != 0:
                    C.setValue(i, j, A_ij * B_ij)
        return C

    def dotDivide(self, B):
        if self.M != B.M or self.N != B.N:
            raise RuntimeException("dotTimes: Matrices are not of the same size!")
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            wordList = self.rows[i].indexList()
            for j, _ in enumerate(wordList):
                A_ij = getValue(i, j)
                B_ij = B.getValue(i, j)
                if A_ij != 0 and B_ij != 0:
                    C.setValue(i, j, A_ij / B_ij)
        return C

    def tfidf(self):
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            wordList = rows[i].indexList()
            for j, _ in enumerate(wordList):
                if self.getValue(i, j) != 0:
                    TF = 1 + log2(getValue(i, j))
                    IDF = log2(double(M) / cols[j].itemCount())
                    C.setValue(i, j, TF * IDF)

        return C

    def tf(self):
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            wordList = rows[i].indexList()
            for j, _ in enumerate(wordList):
                if self.getValue(i, j) != 0:
                    TF = 1 + log2(self.getValue(i, j))
                    C.setValue(i, j, TF)
        return C

    def log2(self, n=None):
        if n is None:
            C = SparseMatrix(self.M, self.N)
            for i in range(self.M):
                indexList = self.getRowRef(i).indexList()
                for j, _ in enumerate(indexList):
                    C.setValue(i, j, 1 + log2(this.getValue(i, j)))
            return C
        else:
            return math.log(n) / math.log(2)

    def rowStochastic(self):
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            sum = rows[i].sum()
            if sum != 0:
                for j, _ in enumearete(self.rows[i].indexList()):
                    C.setValue(i, j, getValue(i, j) / sum)
        return C

    def rowL2Norm(self):
        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            squareSum = rows[i].squareSum()
            if squareSum != 0:
                l2_norm = Math.sqrt(squareSum)
                for j, _ in enumerate(rows[i].indexList()):
                    C.setValue(i, j, getValue(i, j) / l2_norm)
        return C

    def colStochastic(self):
        C = SparseMatrix(self.M, self.N)
        for j in range(self.N):
            sum = this.cols[j].sum()
            if sum != 0:
                for i, _ in enumerate(self.cols[j].indexList()):
                    C.setValue(i, j, this.getValue(i, j) / sum)
        return C

    def selfTimes(self, B):
        if self.N != (B.length())[0]:
            raise RuntimeException("Dimensions disagree")

        for i in range(self.M):
            tmp = SparseVector(self.N)
            for j in range((B.length())[1]):
                x = self.getRowRef(i)
                y = B.getColRef(j)

                if x is not None and y is not None:
                    tmp.setValue(j, x.innerProduct(y))
                else:
                    tmp.setValue(j, 0.0)

            for j in range((B.length())[1]):
                self.setValue(i, j, tmp.getValue(j))

    def plus(self, B):
        A = self
        if A.M != B.M or A.N != B.N:
            raise RuntimeException("Dimensions disagree")

        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            C.rows[i] = A.rows[i].plus(B.rows[i])
        for j in range(self.N):
            C.cols[j] = A.cols[j].plus(B.cols[j])

        return C

    def minus(self, B):
        A = self
        if A.M != B.M or A.N != B.N:
            raise RuntimeException("Dimensions disagree")

        C = SparseMatrix(self.M, self.N)
        for i in range(self.M):
            C.rows[i] = A.rows[i].minus(B.rows[i])
        for j in range(self.N):
            C.cols[j] = A.cols[j].minus(B.cols[j])

        return C

    def makeIdentity(self, n):
        m = SparseMatrix(n, n)
        for i in range(n):
            m.setValue(i, i, 1.0)

        return m

    def makeUniform(self, M, N):
        m = SparseMatrix(M, N)
        for i in range(M):
            for j in range(N):
                m.setValue(i, j, 1.0 / N)

        return m

    def makeRandom(self, M, N, sparseRate):
        if sparseRate <= 0 or sparseRate > 1:
            raise RuntimeException("SparseRate input error!")

        m = SparseMatrix(M, N)
        for i in range(M):
            for j in range(N):
                r = random.random()
                if r < sparseRate:
                    m.setValue(i, j, random.random())

        return m

    def inverse(self):
        if self.M != self.N:
            raise RuntimeException("Dimensions disagree")

        original = self
        newMatrix = makeIdentity(self.M)

        n = self.M

        if n == 1:
            newMatrix.setValue(0, 0, 1 / original.getValue(0, 0))
            return newMatrix

        b = SparseMatrix(original)

        for i in range(n):
            mag = 0
            pivot = -1

            for j in range(i, n):
                mag2 = Math.abs(b.getValue(j, i))
                if mag2 > mag:
                    mag = mag2
                    pivot = j

            if pivot == -1 or mag == 0:
                return newMatrix

            if pivot != i:
                temp = None
                for j in range(i, n):
                    temp = b.getValue(i, j)
                    b.setValue(i, j, b.getValue(pivot, j))
                    b.setValue(pivot, j, temp)

                for j in range(n):
                    temp = newMatrix.getValue(i, j)
                    newMatrix.setValue(i, j, newMatrix.getValue(pivot, j))
                    newMatrix.setValue(pivot, j, temp)

            mag = b.getValue(i, i)
            for j in range(i, n):
                b.setValue(i, j, b.getValue(i, j) / mag)
            for j in range(n):
                newMatrix.setValue(i, j, newMatrix.getValue(i, j) / mag)

            for k in range(n):
                if k == i:
                    continue

                mag2 = b.getValue(k, i)

                for j in range(i, n):
                    b.setValue(k, j, b.getValue(k, j) - mag2 * b.getValue(i, j))
                for j in range(n):
                    newMatrix.setValue(k, j, newMatrix.getValue(k, j) - mag2 * newMatrix.getValue(i, j))

        return newMatrix

    def cholesky(self):
        if self.M != self.N:
            raise RuntimeException("Matrix is not square")

        A = self

        n = A.M
        L = SparseMatrix(n, n)

        for i in range(n):
            for j in range(i + 1):
                sum = 0.0
                for k in range(j):
                    sum += L.getValue(i, k) * L.getValue(j, k)
                if i == j:
                    L.setValue(i, i, math.sqrt(A.getValue(i, i) - sum))
                else:
                    L.setValue(i, j, 1.0 / L.getValue(j, j) * (A.getValue(i, j) - sum))
            if Double.isNaN(L.getValue(i, i)):
                return None

        return L.transpose()

    def covariance(self):
        columnSize = self.N
        cov = SparseMatrix(columnSize, columnSize)

        for i in range(columnSize):
            for j in range(i, columnSize):
                data1 = self.getCol(i)
                data2 = self.getCol(j)
                avg1 = data1.average()
                avg2 = data2.average()

                value = data1.sub(avg1).innerProduct(data2.sub(avg2)) / (data1.length() - 1)
                cov.setValue(i, j, value)
                cov.setValue(j, i, value)

        return cov

    def partScale(self, alpha, indexList):
        if indexList != null:
            for i, in enumerate(indexList):
                for j, _ in enumearte(indexList):
                    self.setValue(i, j, this.getValue(i, j) * alpha)

        return self

    def partPlus(self, B, indexList):
        if indexList is not None:
            if self.M != B.M or self.N != B.N:
                raise RuntimeException("Dimensions disagree")

            for i, _ in enumerate(indexList):
                self.rows[i].partPlus(B.rows[i], indexList)
            for j, _ in enumerate(indexList):
                this.cols[j].partPlus(B.cols[j], indexList)

        return self

    def partMinus(self, B, indexList):
        if indexList is not None:
            if self.M != B.M or self.N != B.N:
                raise RuntimeException("Dimensions disagree")

            for i, _ in enumerate(indexList):
                self.rows[i].partMinus(B.rows[i], indexList)
            for j, _ in enumerate(indexList):
                this.cols[j].partMinus(B.cols[j], indexList)

        return self

    def partTimes(self, x, indexList):
        if indexList is None:
            return x

        b = SparseVector(self.M)

        for i, _ in enumerate(indexList):
            b.setValue(i, self.rows[i].partInnerProduct(x, indexList))

        return b

    def __str__(self):
        s = ""
        for i in range(self.M):
            row = self.getRowRef(i)
            if row.itemCount() == 0:
                continue
            for j, _ in enumerate(row.indexList()):
                s += "(" + i + ", " + j + ": " + this.getValue(i, j) + ") "
            s += "\r\n"

        return s
