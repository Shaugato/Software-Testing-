import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation8MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation8_mr2_search(self):
        print("\n--- Testing MR2 for Mutation 8: Search with Incorrect Error Message ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # Check existence before deletion
        assert self.bst.exists(20), "Node 20 should exist before deletion"
        assert self.bst.exists(10), "Node 10 should exist before deletion"
        assert self.bst.exists(30), "Node 30 should exist before deletion"

        # Try searching for a value that doesn't exist and check the error message
        try:
            self.bst.search(25)
        except ValueError as e:
            assert str(e) == "Node with label 25 does not exist", f"Expected error message for missing node was incorrect: {str(e)}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation8MR2))
