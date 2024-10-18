import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation25MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation25_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 25: Insertion with Tree Properties ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        # Check if the tree structure is as expected
        in_order = [node.label for node in self.bst.inorder_traversal()]
        expected_in_order = [5, 10, 20, 25, 30, 40]
        print(f"In-order traversal obtained: {in_order}")
        assert in_order == expected_in_order, "In-order traversal after insertion failed to reflect correct structure"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation25MR1))
