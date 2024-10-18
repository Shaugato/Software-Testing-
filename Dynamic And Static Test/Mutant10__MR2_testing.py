import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation10MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation10_mr2_search_deletion(self):
        print("\n--- Testing MR2 for Mutation 10: Search and Deletion with Incorrect Traversal ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # Check existence before deletion
        for value in values:
            assert self.bst.exists(value), f"Node {value} should exist before deletion"

        # Delete a value and verify structure
        self.bst.remove(10)
        
        # In-order traversal after deletion
        in_order = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order = [20, 30]
        print(f"In-order traversal after deletion: {in_order}")
        assert in_order == expected_in_order, f"In-order traversal after deletion failed, got: {in_order}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation10MR2))
