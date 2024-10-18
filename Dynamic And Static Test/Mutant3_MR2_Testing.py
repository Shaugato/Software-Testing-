import unittest
from binary_search_tree_recursive import BinarySearchTree, Node


class TestMutation3MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def print_tree_structure(self, node: Node | None, level=0) -> None:
        """ Utility function to print the current tree structure """
        if node is not None:
            self.print_tree_structure(node.right, level + 1)
            print(' ' * 4 * level + '->', node.label)
            self.print_tree_structure(node.left, level + 1)

    def test_mutation3_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 3: Deletion with Node Reassignment ---")

        # Insert values (which are mutated internally)
        values = [10, 5, 15]
        for value in values:
            self.bst.put(value)

        # Print the current tree structure for debugging
        print("\nTree structure after mutation (labels incremented by 1):")
        self.print_tree_structure(self.bst.root)

        # In-order Traversal after insertion (mutated)
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after insertion: {in_order}")
        expected_in_order = [6, 11, 16]  # After mutation
        print(f"Expected in-order traversal: {expected_in_order}")
        assert in_order == expected_in_order, "In-order traversal after insertion did not match expected values."

        # Delete the node with label 11 (originally intended as 10, but mutated to 11)
        self.bst.remove(11)

        # Print the current tree structure for debugging
        print("\nTree structure after deletion (with mutation):")
        self.print_tree_structure(self.bst.root)

        # Perform Traversals after deletion
        in_order_after_deletion = [node.label for node in self.bst.inorder_traversal()]
        post_order_after_deletion = [node.label for node in self.bst.preorder_traversal()]

        # Expected Traversals After Deletion
        expected_in_order_after_deletion = [6, 16]
        expected_post_order_after_deletion = [16, 6]

        # Print actual results
        print(f"In-order traversal after deletion: {in_order_after_deletion}")
        print(f"Expected in-order traversal: {expected_in_order_after_deletion}")
        print(f"Post-order traversal after deletion: {post_order_after_deletion}")
        print(f"Expected post-order traversal: {expected_post_order_after_deletion}")

        # Assertions
        assert in_order_after_deletion == expected_in_order_after_deletion, "In-order traversal after deletion failed to reflect correct structure"
        assert post_order_after_deletion == expected_post_order_after_deletion, "Post-order traversal after deletion failed to reflect correct structure"


# Running tests for Mutation 3 MR2
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation3MR2))
