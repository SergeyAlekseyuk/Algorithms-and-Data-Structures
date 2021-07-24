class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def find_min(self):
        if self.heap_size < 1:
            return 'Heap is empty'
        else:
            return self.heap[0]

    def delete_min(self):
        if self.heap_size < 1:
            return 'Heap is empty'
        else:
            minimum = self.heap[0]
            self.heap[0] = self.heap[self.heap_size - 1]
            self.heap.pop()
            self.heap_size -= 1
            self.sift_down(0)
            return minimum

    def insert(self, item):
        self.heap.append(item)
        self.heap_size += 1
        self.sift_up(self.heap_size - 1)

    def delete(self, i):
        if self.heap_size < 1:
            return 'Heap is empty'
        else:
            if self.heap[i] < self.heap[self.heap_size - 1]:
                self.heap[i] = self.heap[self.heap_size - 1]
                self.heap_size -= 1
                self.sift_down(i)
            else:
                self.heap[i] = self.heap[self.heap_size - 1]
                self.heap_size -= 1
                self.sift_up(i)
            self.heap.pop()

    def sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i):
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < self.heap_size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.heap_size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                return
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

