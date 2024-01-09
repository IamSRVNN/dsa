class ArrayQueue:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data[0]


if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    print(len(Q))
    print(Q.dequeue())
    print(Q.is_empty())
    print(Q.dequeue())
    print(Q.is_empty())
    # print(Q.dequeue())
    Q.enqueue(7)
    Q.enqueue(9)
    print(Q.first())
    Q.enqueue(4)
    print(len(Q))
    print(Q.dequeue())
