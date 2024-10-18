import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation28MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation28_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 28: Deletion with Pre-order Traversal ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(30)

        # Check if the tree structure is as expected after deletion
        pre_order = [node.label for node in self.bst.preorder_traversal()]
        expected_pre_order = [50, 10, 40, 70, 60, 80]
        print(f"Pre-order traversal obtained after deletion: {pre_order}")
        assert pre_order == expected_pre_order, "Pre-order traversal after deletion failed to reflect correct structure"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation28MR2))
