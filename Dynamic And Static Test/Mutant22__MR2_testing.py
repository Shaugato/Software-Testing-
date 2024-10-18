import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation22MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation22_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 22: Deletion with In-Order Traversal Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(10)

        # Expected in-order traversal after deletion
        expected_in_order = [30, 40, 50, 60, 70, 80]
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal obtained after deletion: {in_order}")

        # Assert that the in-order traversal matches the expected sorted order after deletion
        try:
            assert in_order == expected_in_order, f"Expected in-order traversal after deletion to be {expected_in_order}, but got {in_order}"
        except AssertionError as e:
            print(e)
            raise

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation22MR2))
