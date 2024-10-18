import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation14MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation14_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 14: Insertion with Tree Properties ---")

        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.bst.put(value)

        # In-order traversal to verify the correct tree structure
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after insertion: {in_order}")

        # Expected in-order traversal should match the sorted list of inserted values
        expected_in_order = sorted(values)
        assert in_order == expected_in_order, f"In-order traversal after insertion is incorrect, got: {in_order}"

# Running MR1 test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation14MR1))
