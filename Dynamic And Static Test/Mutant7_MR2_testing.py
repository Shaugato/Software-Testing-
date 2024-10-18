import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation7MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation7_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 7: Deletion and Existence Check ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # Check existence before deletion
        assert self.bst.exists(20), "Node 20 should exist before deletion"
        assert self.bst.exists(10), "Node 10 should exist before deletion"
        assert self.bst.exists(30), "Node 30 should exist before deletion"

        # Delete node 20
        self.bst.remove(20)

        # In-order traversal after deletion
        in_order_after = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order_after = [10, 30]
        assert in_order_after == expected_in_order_after, f"In-order traversal after deletion failed, got: {in_order_after}"

        # Check existence after deletion
        assert not self.bst.exists(20), "Node 20 should not exist after deletion"
        assert self.bst.exists(10), "Node 10 should still exist after deletion"
        assert self.bst.exists(30), "Node 30 should still exist after deletion"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation7MR2))
