
from unicodedata import decimal
import unittest
from Queue import Main, Queue, Node


class Tests(unittest.TestCase):

    def test_inputting(self):
        queue = Queue()
        queue.enqueue("Enrique")
        printed = queue.printqueue()
        self.assertEquals("People in your queue are:Enrique, ", printed)

    def test_dequeing(self):
        queue = Queue()
        queue.enqueue("Enrique")
        queue.enqueue("Jorge")
        queue.dequeue()
        printed = queue.printqueue()
        self.assertEquals("People in your queue are:Jorge, ", printed)

    def test_printing(self):
        queue = Queue()
        queue.enqueue("Enrique")
        queue.enqueue("Jorge")
        printed = queue.printqueue()
        self.assertEquals("People in your queue are:Enrique, Jorge, ", printed)


if __name__ == '__main__':
    unittest.main()
