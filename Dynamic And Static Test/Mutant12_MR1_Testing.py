import unittest
from binary_search_tree_recursive import BinarySearchTree, Node

class TestMutation12MR1(unittest.TestCase):
    def setUp(self):
        # Set up a new binary search tree for each test
        self.bst = BinarySearchTree()

    def test_mutation12_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 12: Insertion with Tree Properties ---")

        # Insert distinct values
        values = [15, 10, 25]  
        for value in values:
            self.bst.put(value)

        # Verify tree properties
        assert self.bst.get_max_label() == 25, "Max label should be 25"
        assert self.bst.get_min_label() == 10, "Min label should be 10"

        # In-order traversal should be sorted
        in_order = [node.label for node in self.bst.inorder_traversal()]
        assert in_order == [10, 15, 25], f"In-order traversal failed, got: {in_order}"

        # Pre-order traversal should follow root-left-right
        pre_order = [node.label for node in self.bst.preorder_traversal()]
        assert pre_order == [15, 10, 25], f"Pre-order traversal failed, got: {pre_order}"

# Running tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation12MR1))
