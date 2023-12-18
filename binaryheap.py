
from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    """Abstract Class for Binary Heap."""

    def __init__(self):
        """Pass."""

    @abstractmethod
    def perc_up(self, i):
        """Pass."""

    @abstractmethod
    def insert(self, val):
        """Pass."""

    @abstractmethod
    def perc_down(self, i):
        """Pass."""

    @abstractmethod
    def min_child(self, i):
        """Pass."""

    @abstractmethod
    def remove_min(self):
        """Pass."""


class BinaryHeap(AbstractHeap):
    """Binary Heap Class"""

    def __init__(self):
        self.current_size = 0
        self.heap = [(0)]

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                # Swap value of child with value of its parent
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2

    def insert(self, val):

        self.heap.append(val)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

        """
        Method min_child returns the index of smaller of 2 children of parent at index i
        """

    def min_child(self, i):
        if 2 * i + 1 > self.current_size:  # No right child
            return 2 * i
        if self.heap[2 * i] > self.heap[2 * i + 1]:
            return 2 * i + 1
        return 2 * i

    def perc_down(self, i):
        while 2 * i < self.current_size:
            min_child = self.min_child(i)
            if self.heap[min_child] < self.heap[i]:
                # Swap min child with parent
                self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
            i = min_child


    def remove_min(self):
        ret = self.heap[1]      # the smallest value at beginning
        # Replace it by the last value
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        self.perc_down(1)
        return ret
