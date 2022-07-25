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

    def append(self, item):
        """For appending (i.e. insert at the right-most end of) the linked list"""
        trav = self.head
        while trav and trav.nxt:
            trav = trav.nxt
        trav.nxt = item if type(item) is Node else Node(item)
    
    def prepend(self, item):
        """For prepending (i.e. insert at the left-most end of) the linked list"""
        node = item if type(item) is Node else Node(item)
        node.nxt = self.head
        self.head = node

    def popleft(self):
        """Removes an item from the front-end (left most); basically the root/head node"""
        self.head = self.head.nxt if self.head else None

    def pop(self):
        """Removes the last node from the list"""
        if not self.head or not self.head.nxt:
            self.head = None
        else:
            trav = self.head
            while trav and trav.nxt and trav.nxt.nxt:
                trav = trav.nxt
            trav.nxt = None

    def popright(self):
        """alias for pop()"""
        self.pop()
    

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
head.append(2)
head.append(Node(30, Node(40)))
head.prepend(Node(0))
print(20 in head)
print(head[0])
i = 0
print(head)
for node in head:
    print(node)

head.popleft()
head.pop()
print('After pop')
for node in head:
    print(node)
