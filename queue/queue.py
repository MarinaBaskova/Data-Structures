class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(self.size, item)
    self.size += 1
    return self.storage
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      item_poped = self.storage.pop(0)
      self.size -= 1
      return item_poped

  def len(self):
    self.size = len(self.storage)
    return self.size

test = Queue()
test.storage = [11,22,33]