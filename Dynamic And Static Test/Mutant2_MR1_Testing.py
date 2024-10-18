import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation2MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation2_mr1_is_empty(self):
        print("\n--- Testing MR1 for Mutation 2: Is Tree Empty ---")

        # Initially, the tree should be empty
        is_empty_initial = self.bst.is_empty()
        assert is_empty_initial, f"Tree should be empty initially, but `is_empty()` returned {is_empty_initial}"

        # Insert a value into BST
        self.bst.put(15)

        # After insertion, the tree should not be empty
        is_empty_after_insert = self.bst.is_empty()
        assert not is_empty_after_insert, f"Tree should not be empty after insertion, but `is_empty()` returned {is_empty_after_insert}"

        # Empty the tree
        self.bst.empty()

        # After emptying the tree, it should be empty again
        is_empty_after_empty = self.bst.is_empty()
        assert is_empty_after_empty, f"Tree should be empty after calling `empty()`, but `is_empty()` returned {is_empty_after_empty}"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation2MR1))
