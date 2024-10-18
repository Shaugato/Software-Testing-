import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation4MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation4_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 4: Deletion with Incorrect Comparison ---")

        # Insert values that could potentially lead to incorrect placement due to mutation
        values = [20, 10, 30, 25]

        for value in values:
            try:
                self.bst.put(value)
            except ValueError as e:
                # Print error to highlight that the mutation is causing a ValueError
                print(f"Error encountered while inserting value {value}: {e}")

        # Deleting node 20 (which has two children)
        try:
            self.bst.remove(20)
        except ValueError as e:
            # If the incorrect insertion caused an issue that prevents deletion, print the error
            print(f"Error encountered while deleting value 20: {e}")

        # Expected in-order traversal after deleting root node 20 (original correct logic)
        expected_in_order_after_deletion = [10, 25, 30]

        # Get actual in-order traversal after deletion
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after deletion: {in_order}")
        print(f"Expected in-order traversal after deletion: {expected_in_order_after_deletion}")

        # MR2 should fail if the tree is incorrectly reassigned due to incorrect placement
        assert in_order != expected_in_order_after_deletion, "MR2 should fail due to incorrect node reassignment."

        # Expected post-order traversal after deletion (original correct logic)
        expected_post_order_after_deletion = [10, 30, 25]

        # Get actual post-order traversal after deletion
        post_order = [node.label for node in self.bst.preorder_traversal()]
        print(f"Post-order traversal after deletion: {post_order}")
        print(f"Expected post-order traversal after deletion: {expected_post_order_after_deletion}")

        # MR2 should also fail due to incorrect reassignment affecting the traversal order
        assert post_order != expected_post_order_after_deletion, "MR2 should fail due to incorrect post-order traversal."

# Running tests for MR2 with Mutant 4
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation4MR2))
