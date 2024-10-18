import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation21MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation21_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 21: Deletion with Pre-Order Traversal Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(10)

        # Expected pre-order traversal after deletion
        expected_pre_order = [50, 30, 40, 70, 60, 80]
        pre_order = [node.label for node in self.bst.preorder_traversal()]
        print(f"Pre-order traversal obtained after deletion: {pre_order}")

        # Assert that the pre-order traversal matches the expected order after deletion
        try:
            assert pre_order == expected_pre_order, f"Expected pre-order traversal after deletion to be {expected_pre_order}, but got {pre_order}"
        except AssertionError as e:
            print(e)
            raise

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation21MR2))
