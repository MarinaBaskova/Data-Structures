class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1
    return self.storage
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      item_poped = self.storage.pop()
      self.size -= 1
      return item_poped

  def len(self):
    self.size = len(self.storage)
    return self.size
