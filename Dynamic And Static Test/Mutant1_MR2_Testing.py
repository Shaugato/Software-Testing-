import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation1MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation1_mr2_insertion_after_empty(self):
        print("\n--- Testing MR2 for Mutation 1: Insertion after Emptying the Tree ---")

        # Insert values into BST
        values = [50, 30, 70]
        for value in values:
            self.bst.put(value)

        # Empty the tree
        self.bst.empty()

        # Check if the tree is actually empty
        is_empty = self.bst.is_empty()
        assert is_empty, f"Tree should be empty, but `is_empty()` returned {is_empty}"

        # Insert new value into supposedly empty tree
        self.bst.put(25)

        # Check if the root is correctly assigned to the new value
        assert self.bst.root is not None, "Root should not be None after inserting a new value into an empty tree."
        assert self.bst.root.label == 25, f"Root label should be 25, but got {self.bst.root.label}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation1MR2))
