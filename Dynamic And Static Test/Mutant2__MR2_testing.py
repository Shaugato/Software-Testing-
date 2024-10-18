import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation2MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation2_mr2_is_empty_dependent_logic(self):
        print("\n--- Testing MR2 for Mutation 2: Operations Based on Tree Empty Status ---")

        # Initially, perform an action that relies on the tree being empty
        assert self.bst.is_empty(), "Tree should be empty initially."

        # Insert values to make it non-empty
        self.bst.put(10)
        self.bst.put(20)

        # Empty the tree and check if it's empty
        self.bst.empty()
        assert self.bst.is_empty(), "Tree should be empty after emptying, but it is not."

        # Insert a new value into an empty tree, and verify root assignment
        self.bst.put(5)
        assert self.bst.root is not None, "Root should not be None after inserting a value into an empty tree."
        assert self.bst.root.label == 5, f"Root label should be 5, but got {self.bst.root.label}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation2MR2))
