import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation7MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation7_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 7: Insertion with Tree Properties ---")

        # Insert values into BST
        values = [20, 10, 30]
        for value in values:
            self.bst.put(value)

        # In-order traversal after insertion
        in_order = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order = [10, 20, 30]
        assert in_order == expected_in_order, f"In-order traversal after insertion failed, got: {in_order}"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation7MR1))
