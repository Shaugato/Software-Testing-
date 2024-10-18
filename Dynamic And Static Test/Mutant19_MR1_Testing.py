import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation19MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation19_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 19: Insertion with In-Order Traversal Verification ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        # Expected in-order traversal should be sorted values
        expected_in_order = sorted(values)
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal obtained: {in_order}")

        # Assert that the in-order traversal matches the expected order
        try:
            assert in_order == expected_in_order, f"Expected in-order traversal to be {expected_in_order}, but got {in_order}"
        except AssertionError as e:
            print(e)
            raise

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation19MR1))
