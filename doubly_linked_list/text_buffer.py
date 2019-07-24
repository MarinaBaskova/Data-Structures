from doubly_linked_list import DoublyLinkedList


class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            # for character in init:
            #     self.contents.add_to_tail(character)
            # to dry the code use existing method
            self.append(init)

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s
 #  when adding to the tail of the text buffer

    def append(self, string_to_add):
        for character in string_to_add:
            self.contents.add_to_tail(character)

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct
        # order when adding to the front of the text buffer
        # when you do a[::-1] , it starts from the end, towards the first, taking each element. So it reverses a.
        for character in string_to_add[::-1]:
            self.contents.add_to_head(character)

    # how many char we want to remove from begining or from the end

    def delete_front(self, chars_to_remove):  # number of characters
        while chars_to_remove:
            self.contents.remove_from_head()
            chars_to_remove -= 1

    def delete_back(self, chars_to_remove):
        while chars_to_remove:
            self.contents.remove_from_tail()
            chars_to_remove -= 1

    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer 
    The tail of the concatenated buffer will be the tail of the other buffer 
    The head of the concatenated buffer will be the head of this buffer 
    """
# text1  txt2 ->obj of -> class TextBuffer
# text1 = hello
# text2 = hi
# text1.join(text2)

    def join(self, other_buffer):
        # check if other buffer is empty
        if(other_buffer.contents.length == 0):
            print("Error: Other buffer is empty")
            return
        # we might want to check that other_buffer is indeed a text buffer

        if isinstance(other_buffer, TextBuffer):

             # set self list tail's next node to be the head of the other buffer
            self.contents.tail.next = other_buffer.contents.head
            # set other_buffer head's prev node to be the tail of this buffer
            other_buffer.contents.head.prev = self.contents.tail
            # The head of the concatenated buffer will be the head of this buffer
            # other_buffer.contents.head = self.contents.head
            # The tail of the concatenated buffer will be the tail of the other buffer
            self.contents.tail = other_buffer.contents.tail

            self.contents.length = self.contents.length + other_buffer.contents.length

        else:
            return None

    # if we get fed(joining, what passed in funct) a string instead of a text buffer instance,
    # initialize a new text buffer with this string and then
    # call the join method

    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)


if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

    text.join_string("califragilisticexpealidocious")
    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)
