# tests.py
# Tests of Stack and Queue
# Please exercise them enough to
# show they work under different combinations
# of operations and different orders of those operations
# Modified by: 

import unittest
from stack import Stack
from que import Queue


class TestStack(unittest.TestCase):

    def test_stack_with_ints(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(len(s), 3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(len(s), 1)

        # remove last remaining item
        s.pop()

        # now it should be empty, popping should raise an error
        with self.assertRaises(IndexError):
            s.pop()

    def test_stack_with_strings(self):
        s = Stack()
        s.push("a")
        s.push("b")
        s.push("c")
        self.assertEqual(len(s), 3)
        self.assertEqual(s.peek(), "c")
        self.assertEqual(s.pop(), "c")
        self.assertEqual(s.pop(), "b")
        self.assertEqual(len(s), 1)

        # remove last remaining item
        s.pop()

        # now it should be empty, peeking should raise an error
        with self.assertRaises(IndexError):
            s.peek()


class TestQueue(unittest.TestCase):

    def test_queue_with_ints(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
