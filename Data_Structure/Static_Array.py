"""""""""
Arrays generally are contiguous blocks of memory which means that objects in an array are placed side by side in a sequential manner.
🌟Static Array has a fixed-size preallocation upon creation that is the capacity of the array is specified when created and cannot be modified to take on more objects when the array is full.
"""""""""

class StsticArray:
    def __init__(self,n):
        self.data = [None] * n
    def get_at(self,i):
        if not 0 <= i < len(self.data):
            raise IndexError
        else:
            return self.data[i]
    def set_at(self,i,x):
        if not 0 <= i < len(self.data):
            raise IndexError
        else:
            self.data[i] = x


