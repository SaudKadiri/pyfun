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
        self.head = head or tail    # points to first node of list
        self.tail = tail or head    # points to last node of list

    def insert_after(self, node, new_node):
        new_node.pre = node 
        new_node.nxt = node.nxt   
        if node is self.tail:
            self.tail = new_node
        else:
            node.nxt.prev = new_node
        node.nxt = new_node
    
    def append(self, item):
        node = item if type(item) is Node else Node(item)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.insert_after(self.tail, node)

    def __str__(self):
        # Only for the time being the following prints two values; as it's in testing period once everything is done; a logical str will be returned
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
    dll.append(10)
    dll.insert_after(dll.head, Node(20))
    dll.append(30)
    dll.append(40)
    dll.append(90)
    dll.append(100)
    print(dll)
