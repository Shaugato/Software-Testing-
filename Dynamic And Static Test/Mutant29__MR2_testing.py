import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation29MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation29_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 29: Deletion with Incorrect Lowest Node Access ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Check in-order traversal before deletion
        in_order_before = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal before deletion: {in_order_before}")

        # Delete a node that requires finding the lowest node in the right subtree
        try:
            self.bst.remove(50)
        except Exception as e:
            print(f"Error encountered during deletion: {e}")

        # Check the in-order traversal after deletion
        in_order_after = [node.label for node in self.bst.inorder_traversal()]
        expected_in_order = [10, 30, 40, 60, 70, 80]
        print(f"In-order traversal obtained after deletion: {in_order_after}")
        assert in_order_after == expected_in_order, "In-order traversal after deletion failed to reflect correct structure"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation29MR2))
