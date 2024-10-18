import unittest
from binary_search_tree_recursive import BinarySearchTree, Node


class TestMutation3MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def print_tree_structure(self, node: Node | None, level=0) -> None:
        """ Utility function to print the current tree structure """
        if node is not None:
            self.print_tree_structure(node.right, level + 1)
            print(' ' * 4 * level + '->', node.label)
            self.print_tree_structure(node.left, level + 1)

    def test_mutation3_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 3: Insertion with Incorrect Label ---")

        # Without Mutation (Expected)
        print("\nExpected Output Without Mutation:")
        expected_values = [10, 5, 15]
        print(f"Inserting values: {expected_values}")
        print("Expected In-order Traversal: [5, 10, 15]")
        print("Expected Pre-order Traversal: [10, 5, 15]")

        # With Mutation (Actual)
        print("\nActual Output With Mutation:")
        values = [10, 5, 15]
        for value in values:
            self.bst.put(value)

        # Print the current tree structure for debugging
        print("\nTree structure after mutation (labels incremented by 1):")
        self.print_tree_structure(self.bst.root)

        # Perform Traversals
        in_order = [node.label for node in self.bst.inorder_traversal()]
        pre_order = [node.label for node in self.bst.preorder_traversal()]

        # Print actual results
        print(f"Actual In-order Traversal: {in_order}")
        print(f"Actual Pre-order Traversal: {pre_order}")


# Running tests for Mutation 3 MR1
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation3MR1))
