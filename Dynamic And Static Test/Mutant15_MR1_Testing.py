import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation15MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation15_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 15: Insertion with Existence Check ---")

        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.bst.put(value)

        # Check existence of inserted values
        for value in values:
            exists = self.bst.exists(value)
            print(f"Checking existence of {value}: {exists}")
            assert exists, f"Node {value} should exist but `exists()` returned {exists}"

# Running MR1 test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation15MR1))
