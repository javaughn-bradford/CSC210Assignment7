# stack.py
# A Last In First Out (LIFO) stack
# Modified by:jaaughn bradford 
# Note: Please write this yourself, not using an LLM.
from sequential_collection import SequentialCollection

class Stack(SequentialCollection):

    def push(self, item):
        # add to the top of the stack
        self._data.append(item)

    def pop(self):
        # remove and return the top item
        if len(self._data) == 0:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        # look at the top item without removing it
        if len(self._data) == 0:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    pass
