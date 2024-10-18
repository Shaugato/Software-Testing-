import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation13MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation13_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 13: Deletion with Incorrect Node Reassignment ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.bst.put(value)

        # Delete a value and verify structure
        self.bst.remove(10)  # Remove node 10 (has children)

        # In-order traversal after deletion
        in_order = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order = [5, 15, 20, 25, 30, 35]
        print(f"In-order traversal after deletion: {in_order}")
        assert in_order == expected_in_order, f"In-order traversal after deletion failed, got: {in_order}"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation13MR2))
