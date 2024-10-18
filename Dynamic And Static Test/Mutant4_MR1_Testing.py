import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation4MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation4_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 4: Insertion with Incorrect Comparison ---")

        # Insert values that would lead to the incorrect placement due to '>=' change
        values = [20, 10, 30, 25]

        for value in values:
            try:
                self.bst.put(value)
            except ValueError as e:
                # Print error to highlight that the mutation is causing a ValueError
                print(f"Error encountered while inserting value {value}: {e}")

        # Expected in-order traversal without mutation (original correct logic)
        expected_in_order = [10, 20, 25, 30]

        # Actual in-order traversal after insertion with mutation
        in_order = [node.label for node in self.bst.inorder_traversal()]
        print(f"In-order traversal after insertion: {in_order}")
        print(f"Expected in-order traversal: {expected_in_order}")

        # MR1 should fail due to incorrect placement in the tree
        assert in_order != expected_in_order, "MR1 should fail due to incorrect in-order traversal."

# Running tests for MR1 with Mutant 4
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation4MR1))
