import numpy as np
import math


class DenseMatrix:
    _serialVersionUID = -2069621030647530185

    def __init__(self, numRows=None, numColumns=None, array=None, mat=None):
        if numRows is not None and numColumns is not None:
            self.numRows = numRows
            self.numColumns = numColumns
            self.data = [[] for j in range(self.numColumns)] * self.numRows
        elif array is not None:
            DenseMatrix(len(array), len(array[0]))
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    self.data[i][j] = array[i][j]
        elif mat is not None:
            DenseMatrix(mat.data)

    def clone(self):
        return DenseMatrix(self)

    @staticmethod
    def eye(dim):
        mat = DenseMatrix(dim, dim)
        for i in range(mat.numRows):
            mat.set(i, i, 1.0)
        return mat

    def init(self, mean=None, sigma=None, size=None):
        if mean is not None and sigma is not None:
            for i in range(self.numRows):
                self.data[i] = np.random.normal(mean, sigma, self.numColumns)
        if range is not None:
            for i in range(self.numRows):
                self.data[i] = np.random.uniform(low=0, high=size, size=self.numColumns)
        else:
            self.init(1.0)

    def numRows(self):
        return self.numRows

    def numColumns(self):
        return self.numColumns

    def row(self, rowId, deep=True):
        return DenseVector(data[rowId], deep)

    def column(self, column):
        vec = DenseVector(self.numRows)
        for i in range(self.numRows):
            vec.set(i, self.data[i][column])
        return vec

    def columnMean(self, column):
        sumv = 0.0
        for i in range(self.numRows):
            sumv += self.data[i][column]
        return sumv / self.numRows

    def squaredSum(self):
        res = 0
        for i in range(self.numRows):
            for j in range(self.numColumns):
                res += self.data[i][j] ** 2
        return res

    def norm(self):
        res = self.squaredSum()
        return math.sqrt(res)

    @staticmethod
    def rowMult(m, mrow, n, nrow):
        assert m.numColumns == n.numColumns
        res = 0
        k = m.numColumns
        for j in range(k):
            res += m.get(mrow, j) * n.get(nrow, j)
        return res

    @staticmethod
    def rowMult(m, mcol, n, ncol):
        assert m.numRows == n.numRows
        res = 0
        k = m.numRows
        for j in range(k):
            res += m.get(mcol, j) * n.get(ncol, j)
        return res

    @staticmethod
    def product(m, mrow, n, ncol):
        assert m.numColumns == n.numRows
        res = 0
        for j in range(m.numColumns):
            res += m.get(mrow, j) * n.get(j, ncol)
        return res

    def mult(self, mat=None, vec=None):
        if vec is None:
            assert self.numColumns == mat.numRows
            res = DenseMatrix(self.numRows, mat.numColumns)
            for i in range(res.numRows):
                for j in range(res.numColumns):
                    product = 0
                    for k in range(self.numColumns):
                        product += self.data[i][k] * mat.data[k][j]
                    res.set(i, j, product)
            return res
        else:
            assert self.numColumns == vec.numRows
            res = DenseVector(self.numRows)
            for i in range(self.numRows):
                res.set(i, self.row(i, false).inner(vec))
            return res

    def get(self, row, column):
        return self.data[row][column]

    def set(self, row, column, val):
        self.data[row][column] = val

    def add(self, row=None, column=None, val=None, mat=None):
        if mat is None and row is not None:
            self.data[row][column] += val
        if mat is None and row is None:
            res = DenseMatrix(self.numRows, self.numColumns)
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    res.data[i][j] += self.data[i][j] + val
            return res
        else:
            assert self.numRows == mat.numRows
            assert self.numColumns == mat.numColumns
            res = DenseMatrix(self.numRows, self.numColumns)
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    res.data[i][j] += self.data[i][j] + mat.data[i][j]
            return res

    def scale(self, val):
        mat = DenseMatrix(numRows, numColumns)
        for i in range(self.numRows):
            for j in range(self.numColumns):
                mat.data[i][j] = self.data[i][j] * val
        return mat

    def selfScale(self, val):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                self.data[i][j] = self.data[i][j] * val

    def selfAdd(self, mat):
        assert self.numRows == mat.numRows
        assert self.numColumns == mat.numColumns
        for i in range(self.numRows):
            for j in range(self.numColumns):
                self.data[i][j] += mat.data[i][j]

    def minus(self, mat=None, val=None):
        if val is None:
            assert self.numRows == mat.numRows
            assert self.numColumns == mat.numColumns
            res = DenseMatrix(self.numRows, self.numColumns)
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    res.data[i][j] = self.data[i][j] - mat.data[i][j]
            return res
        else:
            res = DenseMatrix(self.numRows, self.numColumns)
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    res.data[i][j] = self.data[i][j] - val
            return res

    def cholesky(self):
        if self.numRows != self.numColumns:
            raise RuntimeException("Matrix is not square")

        n = self.numRows
        L = DenseMatrix(n, n)

        for i in range(n):
            for j in range(i + 1):
                sum = 0.0
                for k in range(j):
                    sum += L.get(i, k) * L.get(j, k)

                if i == j:
                    val = math.sqrt(self.data[i][i] - sum)
                else:
                    val = (self.data[i][j] - sum) / L.get(j, j)
                L.set(i, j, val)

            if Double.isNaN(L.get(i, i)):
                return nullptr

        return L.transpose()

    def transpose(self):
        mat = DenseMatrix(self.numColumns, self.numRows)

        for i in range(mat.numRows):
            for j in range(mat.numColumns):
                mat.set(i, j, this.data[j][i])

        return mat

    def cov(self):
        mat = DenseMatrix(self.numColumns, self.numColumns)

        for i in range(self.numColumns):
            xi = self.column(i)
            xi = xi.minus(xi.mean())

            mat.set(i, i, xi.inner(xi) / (xi.size - 1))

            for j in range(i + 1, self.numColumns):
                yi = this.column(j)
                val = xi.inner(yi.minus(yi.mean())) / (xi.size - 1)

                mat.set(i, j, val)
                mat.set(j, i, val)

        return mat

    def inverse(self):
        if numRows != numColumns
            raise RuntimeException("Only square matrix can do inversion");

        n = numRows
        mat = DenseMatrix(self)

        if n == 1:
            mat.set(0, 0, 1.0 / mat.get(0, 0))
            return mat

        row = []
        col = []
        temp = []

        for k in range(n):
            row[k] = k
            col[k] = k

        for k in range(n):
            pivot = mat.get(row[k], col[k])
            I_pivot = k
            J_pivot = k
            for i in range(k,n):
                for j in range(k,n):
                    abs_pivot = math.abs(pivot)
                    if math.abs(mat.get(row[i], col[j])) > abs_pivot:
                        I_pivot = i
                        J_pivot = j
                        pivot = mat.get(row[i], col[j])



            if Math.abs(pivot) < 1.0E-10:
                raise RuntimeException("Matrix is singular !");

            hold = row[k]
            row[k] = row[I_pivot]
            row[I_pivot] = hold
            hold = col[k]
            col[k] = col[J_pivot]
            col[J_pivot] = hold

            mat.set(row[k], col[k], 1.0 / pivot)
            for j in range(n):
                if j != k:
                    mat.set(row[k], col[j], mat.get(row[k], col[j]) * mat.get(row[k], col[k]))

            for i in range(n):
                if k != i:
                    for j in range(n):
                        if k != j:

                            val = mat.get(row[i], col[j]) - mat.get(row[i], col[k]) * mat.get(row[k], col[j])
                            mat.set(row[i], col[j], val)

                    mat.set(row[i], col[k], -mat.get(row[i], col[k]) * mat.get(row[k], col[k]))

        for j in range(n):
            for i in range(n):
                temp[col[i]] = mat.get(row[i], j)

            for i in range(n):
                mat.set(i, j, temp[i])

        for i in range(n):
            for j in range(n):
                temp[row[j]] = mat.get(i, col[j])

            for j in range(n):
                mat.set(i, j, temp[j])
                
        return mat

    def inv(self):
        if this.numRows != this.numColumns:
            raise RuntimeException("Dimensions disagree")

        n = self.numRows
        mat = DenseMatrix.eye(n)

        if n == 1:
            mat.set(0, 0, 1 / self.get(0, 0))
            return mat

        b = DenseMatrix(self)

        for i in range(n):
            mag = 0
            pivot = -1

            for j in range(i, n):
                mag2 = math.abs(b.get(j, i))
                if mag2 > mag:
                    mag = mag2
                    pivot = j

            if pivot == -1 or mag == 0:
                return mat

            if pivot != i:
                for j in range(i, n):
                    temp = b.get(i, j)
                    b.set(i, j, b.get(pivot, j))
                    b.set(pivot, j, temp)

                for j in range(n):
                    temp = mat.get(i, j)
                    mat.set(i, j, mat.get(pivot, j))
                    mat.set(pivot, j, temp)

            mag = b.get(i, i)
            for j in range(i, n):
                b.set(i, j, b.get(i, j) / mag)

            for j in range(n):
                mat.set(i, j, mat.get(i, j) / mag)

            for k in range(n):
                if k == i:
                    continue
                mag2 = b.get(k, i)

                for j in range(i, n):
                    b.set(k, j, b.get(k, j) - mag2 * b.get(i, j))

                for j in range(n):
                    mat.set(k, j, mat.get(k, j) - mag2 * mat.get(i, j))

        return mat

    def setRow(self, row, val=None, vals=None):
        if val is not None:
            for i in range(len(self.data[row])):
                self.data[row][i] = val
        else:
            for j in range(self.numColumns):
                self.data[row][j] = vals.data[j]

    def clear(self):
        for i in range(self.numRows):
            self.setRow(i, 0.0)

    def __str__(self):
        return str(self.data)
