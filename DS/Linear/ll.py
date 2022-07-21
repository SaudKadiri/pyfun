class Node:
    def __init__(self, val, nxt=None):
        """Initializes the vals and nxr"""
        self.val = val
        self.nxt = nxt
    
    def __repr__(self):
        """For user-friendly output"""
        return 'Node({})'.format(self.val)

class LinkedList:
    """Linked List Class in Python"""
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        """For appending (i.e. insert at the right-most end of) the linked list"""
        trav = self.head
        while trav and trav.nxt:
            trav = trav.nxt
        trav.nxt = node
    
    def prepend(self, node):
        """For prepending (i.e. insert at the left-most end of) the linked list"""
        node.nxt = self.head
        self.head = node

    def at(self, n):
        """Ordinal Traversal"""
        trav, i = self.head, 1
        while i < n and trav:
            trav = trav.nxt
            i += 1
        return trav
    
    def __getitem__(self, i):
        """Indices for the list"""
        return self.at(i+1)

    def count(self):
        """length of the list"""
        trav = self.head
        cnt = 0
        while trav:
            cnt += 1
            trav = trav.nxt
        return cnt

    def __len__(self):
        """len function for the list"""
        return self.count()
    
    def __contains__(self, val):
        """magic method for `in` keywod"""
        trav = self.head
        while trav:
            if trav.val == val:
                return True
            trav = trav.nxt
        return False

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nxt

    def __str__(self):
        """User-friendly output"""
        trav, nodes = self.head, []
        while trav:
            nodes.append(f'Node({trav.val})')
            trav = trav.nxt
        return ' -> '.join(nodes)
    
head = LinkedList(Node(10))
head.append(Node(20))
head.append(Node(30, Node(40)))
head.prepend(Node(0))
print(10 in head)
print(head[0])
i = 0
print(head)
for node in head:
    print(node)
