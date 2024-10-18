import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation23MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation23_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 23: Insertion with Pre-Order Traversal Verification ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        # Expected pre-order traversal
        expected_pre_order = [20, 10, 5, 30, 25, 40]
        pre_order = [node.label for node in self.bst.preorder_traversal()]
        print(f"Pre-order traversal obtained: {pre_order}")

        # Assert that the pre-order traversal matches the expected order
        try:
            assert pre_order == expected_pre_order, f"Expected pre-order traversal to be {expected_pre_order}, but got {pre_order}"
        except AssertionError as e:
            print(e)
            raise

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation23MR1))
