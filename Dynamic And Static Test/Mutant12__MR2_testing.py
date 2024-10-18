import unittest
from binary_search_tree_recursive import BinarySearchTree, Node

class TestMutation12MR2(unittest.TestCase):
    def setUp(self):
        # Set up a new binary search tree for each test
        self.bst = BinarySearchTree()

    def test_mutation12_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 12: Deletion with Incorrect Condition ---")

        # Insert distinct values to form a base tree structure
        values = [50, 30, 60, 80]
        for value in values:
            self.bst.put(value)

        # In-order traversal before deletion
        in_order_before = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal before deletion: {in_order_before}")

        # Expected in-order traversal before deletion
        expected_in_order_before = [30, 50, 60, 80]
        assert in_order_before == expected_in_order_before, "In-order traversal before deletion is incorrect."

        # Delete node 60, which has one child (80)
        self.bst.remove(60)

        # In-order traversal after deletion
        in_order_after = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after deletion: {in_order_after}")

        # Expected in-order traversal after deletion
        expected_in_order_after = [30, 50, 80]
        assert in_order_after == expected_in_order_after, f"In-order traversal after deletion failed, got: {in_order_after}"

        # Post-order traversal after deletion
        post_order = [node.label for node in self.bst.preorder_traversal()]
        print(f"Post-order traversal after deletion: {post_order}")

        # Expected post-order traversal after deletion
        expected_post_order = [50, 30, 80]
        assert post_order == expected_post_order, f"Post-order traversal after deletion failed, got: {post_order}"

# Running tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation12MR2))
