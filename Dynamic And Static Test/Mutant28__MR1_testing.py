import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation28MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation28_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 28: Insertion with Pre-order Traversal ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        # Check if the pre-order traversal is as expected
        pre_order = [node.label for node in self.bst.preorder_traversal()]
        expected_pre_order = [20, 10, 5, 30, 25, 40]
        print(f"Pre-order traversal obtained: {pre_order}")
        assert pre_order == expected_pre_order, "Pre-order traversal after insertion failed to reflect correct structure"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation28MR1))
