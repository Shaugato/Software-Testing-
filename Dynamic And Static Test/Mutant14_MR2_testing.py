import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation14MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation14_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 14: Deletion with Incorrect Node Reassignment ---")

        # Insert values to form a tree
        values = [50, 30, 70, 60, 80]
        for value in values:
            self.bst.put(value)

        # Perform in-order traversal before deletion
        in_order_before = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal before deletion: {in_order_before}")
        
        # Expected in-order before deletion
        expected_in_order_before = sorted(values)
        assert in_order_before == expected_in_order_before, "In-order traversal before deletion is incorrect."

        # Remove node 70, which has two children (60 and 80)
        self.bst.remove(70)

        # Perform in-order traversal after deletion
        in_order_after = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after deletion: {in_order_after}")

        # Expected in-order traversal after deletion
        expected_in_order_after = [30, 50, 60, 80]  # 70 should be removed
        assert in_order_after == expected_in_order_after, f"In-order traversal after deletion is incorrect, got: {in_order_after}"

        # Perform post-order traversal after deletion
        post_order = [node.label for node in self.bst.preorder_traversal()]
        print(f"Post-order traversal after deletion: {post_order}")

        # Expected post-order traversal after deletion
        expected_post_order = [50, 30, 60, 80]
        assert post_order == expected_post_order, f"Post-order traversal after deletion failed, got: {post_order}"

# Running MR2 test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation14MR2))
