class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def append(self,new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node


    def delete(self,value):
        curr = self.head
        dummy = Node(None)
        dummy.next = curr
        prev = dummy

        while curr:
            nxt = curr.next
            if curr.value == value:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt

    def insert(self,new_element,position):
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next




