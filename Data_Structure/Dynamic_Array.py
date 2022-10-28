# In python, there is no way to specify the capacity of an array upfront when it is instantiated
# python arrays use resizable vectors under the hood and this works whenever adding an object to an array that has already reached its maximum capacity, a new array is reallocated with the capacity to hold twice as much as the previous array.
# As a result, python arrays are dynamic and are called Lists.

class DynamicArray:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1)
        self.copy_forward(0, i, A, 0)
        A[i] = x
        self.copy_forward(i, n - 1, A, i + 1)
        self.build(A)

    def delete_at(self, i, x):
        n = len(self)
        A = [None] * (n - 1)
        self.copy_forward(0, i, A, 0)
        x = self.A[i]
        self.copy_forward(i + 1, n - i - 1, A, i + 1)
        self.build(A)
        return x

    def insert_first(self,x):
        self.insert_at(0,x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self,x):
        self.insert_at(len(self),x)

    def delete_last(self):
        return self.delete_at(len(self)-1)



