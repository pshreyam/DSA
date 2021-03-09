import unittest
from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
    
    def tearDown(self):
        del self.ll
    
    def test_add_to_head(self):
        self.assertEqual(self.ll.traverse(), "List Empty!")
        self.ll.add_to_head(20)
        self.assertEqual(self.ll.traverse(), "20")
        self.ll.add_to_head(40)
        self.assertEqual(self.ll.traverse(), "40 -> 20")
    
    def test_add_to_tail(self):
        self.assertEqual(self.ll.traverse(), "List Empty!")
        self.ll.add_to_tail(100)
        self.assertEqual(self.ll.traverse(), "100")
        self.ll.add_to_tail(200)
        self.assertEqual(self.ll.traverse(), "100 -> 200")
    
    def test_delete_from_head(self):
        self.ll.add_to_head(20)
        self.ll.add_to_head(40)
        self.ll.add_to_tail(100)
        self.ll.add_to_tail(200)
        self.ll.delete_from_head()
        self.assertEqual(self.ll.traverse(), "20 -> 100 -> 200")
    
    def test_delete_from_tail(self):
        self.ll.add_to_head(20)
        self.ll.add_to_head(40)
        self.ll.add_to_tail(100)
        self.ll.add_to_tail(200)
        self.ll.delete_from_tail()
        self.assertEqual(self.ll.traverse(), "40 -> 20 -> 100")
        self.ll.delete_from_tail()
        self.assertEqual(self.ll.traverse(), "40 -> 20")
    
    def test_search(self):
        self.ll.add_to_head(20)
        self.ll.add_to_head(40)
        self.ll.add_to_tail(100)
        self.ll.add_to_tail(200)
        self.assertEqual(self.ll.search(200), True)
        self.assertEqual(self.ll.search(2), False)
        self.ll.delete_from_tail()
        self.assertEqual(self.ll.search(200), False)


if __name__ == "__main__":
    unittest.main()