import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation29MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation29_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 29: Insertion with Tree Properties ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.bst.put(value)

        # Check in-order traversal to ensure correct structure
        in_order = [node.label for node in self.bst.inorder_traversal()]
        expected_in_order = [5, 10, 15, 20, 25, 30, 35]
        print(f"In-order traversal obtained: {in_order}")
        assert in_order == expected_in_order, "In-order traversal after insertion failed to reflect correct structure"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation29MR1))
