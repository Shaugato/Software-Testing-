import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation6MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation6_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 6: Deletion after Insertion ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # In-order traversal before deletion
        in_order_before = [i.label for i in self.bst.inorder_traversal()]
        print(f"In-order traversal before deletion: {in_order_before}")

        # Delete node 10
        self.bst.remove(10)

        # In-order traversal after deletion
        in_order_after = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order_after = [20, 30]
        assert in_order_after == expected_in_order_after, f"In-order traversal after deletion failed, got: {in_order_after}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation6MR2))
