class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.value:
            return None
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):  # o(logn)
        if target == self.value:
            return True

        if target < self.value:  # if true we go left
            if self.left is None:  # if it is not there we are done
                return False
            else:  # we keep searching left
                return self.left.contains(target)
        elif target > self.value:  # if true we go right
            if self.right is None:  # if it is not there we are done
                return False
            else:
                # we keep searching right until we find the answer
                return self.right.contains(target)

    def get_max(self):
      # if not self:
      # return None
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

            """
            while self.right is not None:
            self = self.right
        return self.value
            """
    # O(log n) we are cutting tree half evrytime

    def for_each(self, cb):
        cb(self.value)
        # DFS
        # self left exist then call for each on the left
        if self.left:
          # we dont need the return, because if we do it will exit the function before calling it on self.right
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
