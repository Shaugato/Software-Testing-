import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation1MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation1_mr1_empty(self):
        print("\n--- Testing MR1 for Mutation 1: Emptying the Tree ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # Empty the tree
        self.bst.empty()

        # Check if the tree is actually empty
        is_empty = self.bst.is_empty()
        assert is_empty, f"Tree should be empty, but `is_empty()` returned {is_empty}"

        # Check if the root is None
        assert self.bst.root is None, "Tree root should be None after calling `empty()`, but it is not."

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation1MR1))
