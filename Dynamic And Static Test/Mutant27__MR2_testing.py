import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation27MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation27_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 27: Deletion with Tree Properties Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(30)

        # Check if the tree structure is as expected after deletion
        in_order = [node.label for node in self.bst.inorder_traversal()]
        expected_in_order = [10, 40, 50, 60, 70, 80]
        print(f"In-order traversal obtained after deletion: {in_order}")
        assert in_order == expected_in_order, "In-order traversal after deletion failed to reflect correct structure"

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation27MR2))
