# Author: Saud
# Reference: https://en.wikipedia.org/wiki/Doubly_linked_list

class Node:
    def __init__(self, val, nxt=None, pre=None):
        """Initializes the vals and nxt"""
        self.pre = pre
        self.val = val
        self.nxt = nxt
    
    def __repr__(self):
        """For user-friendly output"""
        return 'Node({})'.format(self.val)

class DoublyLinkedList:
    def __init__(self, head=None, tail=None) -> None:
        """If some head or tail is passed initializes it with it; else assigns None"""
        self.head = head or tail    # points to first node of list
        self.tail = tail or head    # points to last node of list

    def insert_after(self, node, new_node):
        """Insert the new_node after node"""
        new_node.pre = node 
        new_node.nxt = node.nxt   
        if node is self.tail:
            self.tail = new_node
        else:
            node.nxt.pre = new_node
        node.nxt = new_node

    def append(self, item):
        """Insertion at the rear (right) end of the list"""
        node = item if type(item) is Node else Node(item)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.insert_after(self.tail, node)

    def insert_before(self, node, new_node):
        """Inser a new_node before node"""
        new_node.nxt = node
        new_node.pre = node.pre
        if node is self.head:
            self.head = new_node
        else:
            node.pre.nxt = new_node
        node.pre = new_node

    def prepend(self, item):
        """Insert at the front (left) end of the list"""
        node = item if type(item) is Node else Node(item)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.insert_before(self.head, node)

    def remove_left(self):
        if self.head is not None:
            self.head = self.head.nxt
            self.head.pre = None
    
    def remove_right(self):
        if self.tail is not None:
            self.tail = self.tail.pre
            self.tail.nxt = None

    def __str__(self):
        """User-friendly output"""
        trav, nodes = self.head, []
        while trav:
            nodes.append(f'Node({trav.val})')
            trav = trav.nxt
        ltor = ' ⇄ '.join(nodes)

        trav, nodes = self.tail, []
        while trav:
            nodes.append(f'Node({trav.val})')
            trav = trav.pre
        rtol = ' ⇄ '.join(nodes[::-1])
        return f'left to right: {ltor}\nright to left: {rtol}'

    

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.prepend(10)
    dll.insert_after(dll.head, Node(20))
    dll.prepend(30)
    dll.prepend(40)
    dll.prepend(90)
    dll.prepend(100)
    dll.prepend(1110)
    print(dll)
    dll.remove_left()
    dll.remove_right()
    print(dll)
