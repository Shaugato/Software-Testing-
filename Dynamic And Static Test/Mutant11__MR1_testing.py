import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation11MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation11_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 11: Insertion with Incorrect Search Return ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # Check existence after insertion
        for value in values:
            exists = self.bst.exists(value)
            print(f"Checking existence of {value}: {exists}")
            assert exists, f"Node {value} should exist but `exists()` returned {exists}"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation11MR1))
