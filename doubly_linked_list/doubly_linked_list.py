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
        new_node = ListNode(value, prev=None, next=None)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def remove_from_head(self):
        if (self.length == 0):
            return None
        old_head = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = old_head.next
            self.head.prev = None
            old_head.next = None
        self.length -= 1
        return old_head.value

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
        return popped_node.value

    def move_to_front(self, node):
        if node is self.head:
            return node

        if node is self.tail:
            self.remove_from_tail()

        else:
            node.delete()
            self.length -= 1
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node is self.tail:
            return node
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1

        self.add_to_tail(node.value)

    def delete(self, node):
        if self.head is self.tail:
            self.remove_from_head()
        elif self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail()

    def get_max(self):
        if not self.head:
            return None
        # set our starting max value as the first value we'll begin looping through in the list, the head
        max_value = self.head.value
        # set a current value to check against
        current = self.head

        while current:
            if current.value > max_value:
                max_value = current.value
            # increment current
            current = current.next
        return max_value


list = DoublyLinkedList()

# list.add_to_tail(10)
# list.add_to_tail(11)
# list.add_to_tail(12)
# # list.remove_from_tail()
# # list.remove_from_tail()
# # list.remove_from_tail()
# # list.remove_from_head()
# list.add_to_head(9)
# list.add_to_head(8)
# print(list)
# def delete(self, node): --> Takes a reference to a node in the list and removes it from the list.
# The deleted node's `previous` and `next` pointers should point to each afterwards.


# test_list_move_to_front
# test_list_remove_from_head
# test_list_remove_from_tail
