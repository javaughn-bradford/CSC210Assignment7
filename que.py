# que.py
# A First In First Out (FIFO) queue
# Modified by:javaughn bradford 
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection


class Queue(SequentialCollection):

    def push(self, item):
        # add to the end of the queue
        self._data.append(item)

    def pop(self):
        # remove and return from the front
        if len(self._data) == 0:
            raise IndexError("pop from empty queue")
        return self._data.pop(0)

    def peek(self):
        # look at the first item without removing it
        if len(self._data) == 0:
            raise IndexError("peek from empty queue")
        return self._data[0]


    pass
