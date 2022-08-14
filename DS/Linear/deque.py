from dll import DoublyLinkedList

class Deque:
    def __init__(self, seq=[]) -> None:
        self._queue = DoublyLinkedList()
        for item in seq:
            self._queue.append(item)
        
    
    def append(self, item) -> None:
        self._queue.append(item)
    
    def prepend(self, item) -> None:
        self._queue.prepend(item)

    def popleft(self):
        val = self._queue.head.val
        self._queue.remove_left()
        return val
    
    def popright(self):
        val = self.queue.tail.val
        self._queue.remove_right()
        return val

    def __str__(self) -> str:
        return self._queue.__str__()

if __name__ == '__main__':
    dq = Deque()
    print(dq)
    dq.append(10)
    dq.prepend(9)
    print(dq)
    # print(dq.popleft())
    # print(dq.popright())
    # print(dq.popleft())
    print(dq)
