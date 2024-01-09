Another fundamental data structure is the queue. It is a close “cousin” of the stack,
as a queue is a collection of objects that are inserted and removed according to the
first-in, first-out (FIFO) principle. That is, elements can be inserted at any time,
but only the element that has been in the queue the longest can be next removed.

The queue abstract data type (ADT)supports the following two fundamental methods for a queue Q:
- Q.enqueue(e): Add element e to the back of queue Q.
- Q.dequeue( ): Remove and return the first element from queue Q; an error occurs if the queue is empty.

The queue ADT also includes the following supporting methods (with first being analogous to the stack’s top method):
- Q.first(): Return a reference to the element at the front of queue Q, without removing it; an error occurs if the queue is empty.
- Q.is empty( ): Return True if queue Q does not contain any elements.
- len(Q): Return the number of elements in queue Q; in Python, we implement this with the special method \__len__.