"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)
    if (self.length == 0):
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head  
      self.head = new_node
      # self.head.insert_before(value)
      # self.head = self.head.prev

    self.length += 1

  def remove_from_head(self):
    if (self.length == 0):
      return None
    old_head =  self.head

    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = old_head.next
      self.head.prev = None
      old_head.next = None

    self.length -= 1  
    

  def add_to_tail(self, value):
    new_list_node = ListNode(value)
    if (self.length == 0):
      self.head = new_list_node
      self.tail = new_list_node
    else:
        self.tail.insert_after(value)
        self.tail = self.tail.next

    self.length += 1
    # return new_list_node     

  def remove_from_tail(self):
    
    if self.length == 0:
      return None

    popped_node = self.tail 

    if self.length == 1:
      self.head = None
      self.tail = None
    else:  
      self.tail = popped_node.prev
      self.tail.next = None
      popped_node.prev = None

    self.length -= 1    


  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass


list = DoublyLinkedList()

list.add_to_tail(10)
list.add_to_tail(11)
list.add_to_tail(12)
# list.remove_from_tail()
# list.remove_from_tail()
# list.remove_from_tail()
# list.remove_from_head()
list.add_to_head(9)
list.add_to_head(8)
print(list)
print()