class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # Delete the node that contains the value you want deleted in the heap
        # Replace the deleted node with the farthest right node.
        deleted_node = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        self._sift_down(0)
        return deleted_node

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] <= self.storage[parent]:
                break
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            index = parent

    def _sift_down(self, index):
        parent_index = index
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        if len(self.storage) > left_child and self.storage[parent_index] < self.storage[left_child]:
            parent_index = left_child
        if len(self.storage) > right_child and self.storage[parent_index] < self.storage[right_child]:
            parent_index = right_child
        if parent_index is not index:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self._sift_down(parent_index)
